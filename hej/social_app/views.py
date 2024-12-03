""" Views for the social app. """

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from social_app.models import UserProfile, Post, Comment
from social_app.forms import UserForm, UserProfileInfoForm, CommentForm


app_name = "social_app"  # Used for namespacing URLs in templates


@login_required
def user_profile(request, user_id=None):
    """Render the user profile with posts and nested comments."""

    current_user_profile_info = UserProfile.objects.filter(user=request.user).first()

    if user_id is None:
        user_user = request.user
    else:
        user_user = get_object_or_404(User, id=user_id)

    user_profile_info = UserProfile.objects.filter(user=user_user).first()

    if request.method == "POST" and user == request.user:
        form = UserProfileInfoForm(
            request.POST, request.FILES, instance=user_profile_info
        )
        if form.is_valid():
            form.save()
            return redirect("user_profile", user_id=user_user.id)
    else:
        form = UserProfileInfoForm(instance=user_profile_info)

    # Fetch the user's profile and posts
    user_posts = Post.objects.filter(user=user_user).order_by("-created_at")

    posts_with_comments = []
    for post in user_posts:
        # Fetch the top-level comments for the post
        top_level_comments = post.comments.filter(parent=None).order_by("-created_at")[
            :2
        ]

        # For each top-level comment, fetch its replies (nested comments)
        comments_with_replies = []
        for comment in top_level_comments:
            replies = comment.replies.all().order_by("created_at")
            comments_with_replies.append({"comment": comment, "replies": replies})

        posts_with_comments.append({"post": post, "comments": comments_with_replies})

    this_is_me = user_user.id == request.user.id

    context = {
        "user_id": user_user.id,
        "username": user_user.username,
        "profile_pic": (
            user_profile_info.profile_pic.url
            if user_profile_info.profile_pic
            else False
        ),
        "about": user_profile_info.bio if user_profile_info else "",
        "email": user_user.email,
        "user_profile": user_profile_info,
        "posts_with_comments": posts_with_comments,
        "this_is_me": this_is_me,
        "current_user_profile_info": current_user_profile_info,
    }

    return render(request, "social-app/user_profile.html", context)


@login_required
def search_user(request):
    """Render the search page."""

    current_user_profile_info = UserProfile.objects.filter(user=request.user).first()

    if "SearchQuery" in request.GET:
        # get all users
        # users=User.object.all()
        data = None

        # search_query = request.GET.get("SearchQuery")
        search_query = get_object_or_404(request.GET, "SearchQuery")

        # using Query tool to add multiple quries to get data from model
        data = User.objects.filter(Q(username__icontains=search_query)).select_related(
            "userprofile"
        )

        context = {"data": data, "current_user_profile_info": current_user_profile_info}
        return render(request, "social-app/search.html", context)
    else:
        context = {"current_user_profile_info": current_user_profile_info}
        return render(request, "social-app/user_profile.html", context)
        # return HttpResponse("No search query provided.")

    return HttpResponse("Invalid request method.")


@login_required
def followers(request):
    """Render the search page."""

    current_user_profile_info = UserProfile.objects.filter(user=request.user).first()
    context = {"current_user_profile_info": current_user_profile_info}

    return render(request, "social-app/followers.html", context)


@login_required
def following(request):
    """Render the search page."""

    current_user_profile_info = UserProfile.objects.filter(user=request.user).first()
    context = {"current_user_profile_info": current_user_profile_info}

    return render(request, "social-app/following.html", context)


@login_required
def feed(request):
    """Render the search page."""

    current_user_profile_info = UserProfile.objects.filter(user=request.user).first()
    context = {"current_user_profile_info": current_user_profile_info}

    return render(request, "social-app/feed.html", context)


def register(request):
    """Register a new user."""

    if request.user.is_authenticated:
        return redirect("social_app:feed")

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            try:
                # Save user instance
                user = user_form.save(commit=False)

                # Check if email is unique
                if User.objects.filter(email=user.email).exists():
                    raise ValidationError("A user with this email already exists.")

                # Save password and finalize user creation
                user.set_password(user.password)
                user.save()

                # Save profile instance
                profile = profile_form.save(commit=False)
                profile.user = user

                # Save profile picture if provided
                if "profile_picture" in request.FILES:
                    profile.profile_picture = request.FILES["profile_picture"]

                profile.save()
                registered = True

            except ValidationError as e:
                user_form.add_error("email", e.message)
            except IntegrityError:
                user_form.add_error(None, "An error occurred during registration.")
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(
        request,
        "social-app/registration.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
        },
    )


def login_view(request):
    """Log in a user."""
    if request.user.is_authenticated:
        return redirect("social_app:feed")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("social_app:feed")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "social-app/login.html")


def custom_logout_view(request):
    """Log out a user."""
    logout(request)  # Logs out the user
    return redirect("social_app:login")  # Redirect to the homepage (or another page)


@login_required
def view_post(request, post_id):
    """View a specific post and handle comments."""

    current_user_profile_info = UserProfile.objects.filter(user=request.user).first()

    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_at")
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect("social_app:view_post", post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "social-app/view_post.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
            "current_user_profile_info": current_user_profile_info,
        },
    )
