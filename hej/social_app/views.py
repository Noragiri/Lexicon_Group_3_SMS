""" Views for the social app. """

from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import IntegrityError
from social_app.models import UserProfile, Post
from social_app.forms import UserForm, UserProfileInfoForm


app_name = "social_app"


@login_required
def user_profile(request, user_id=0):
    """Render the user profile."""

    # If no user_id is provided, show a default user profile (or a placeholder for now)
    if user_id == 0:
        context = {
            "username": "Guest",
            "profile_pic": None,
            "about": "This is a guest profile. Log in or specify a user ID to view a profile.",
            "email": "guest@example.com",
            "user_posts": [],
        }
        return render(request, "social-app/user_profile.html", context)

    # Fetch the user and their profile by ID
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    user_posts = Post.objects.filter(user=user).order_by("-created_at")

    context = {
        "user_id": user.id,
        "username": user.username,
        "profile_pic": (
            user_profile.profile_pic.url if user_profile.profile_pic else None
        ),
        "about": user_profile.bio,
        "email": user.email,
        "user_profile": user_profile,
        "user_posts": user_posts,
    }

    # Fake data just added to display something

    fakeposts = [
        {
            "post_id": 1,
            "name": "Name Namesson",
            "date": "2024-12-04",
            "message": "Oyeah this and that",
        },
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {
            "post_id": 2,
            "name": "John Smith",
            "date": "2024-12-06",
            "message": "Yet another post content",
        },
        {
            "post_id": 3,
            "name": "Name Namesson",
            "date": "2024-12-04",
            "message": "Oyeah this and that",
        },
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {
            "post_id": 4,
            "name": "John Smith",
            "date": "2024-12-06",
            "message": "Yet another post content",
        },
    ]

    context = {
        "user_id": user_id,
        "username": "Alice",
        "password": "password",
        "profile_pic": "https://www.fillmurray.com/200/300",
        "about": "I am a software engineer.",
        "email": "hej@hej.com",
        "posts": fakeposts,
    }

    return render(request, "social-app/user_profile.html", context)


@login_required
def user_profile_no_id(request, user_id=0):
    """Render the user profile."""

    # Fake data just added to display something

    fakeposts = [
        {
            "post_id": 1,
            "name": "Name Namesson",
            "date": "2024-12-04",
            "message": "Oyeah this and that",
        },
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {
            "post_id": 2,
            "name": "John Smith",
            "date": "2024-12-06",
            "message": "Yet another post content",
        },
        {
            "post_id": 3,
            "name": "Name Namesson",
            "date": "2024-12-04",
            "message": "Oyeah this and that",
        },
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {
            "post_id": 4,
            "name": "John Smith",
            "date": "2024-12-06",
            "message": "Yet another post content",
        },
    ]

    context = {
        "user_id": user_id,
        "username": "Alice",
        "password": "password",
        "profile_pic": "https://www.fillmurray.com/200/300",
        "about": "I am a software engineer.",
        "email": "hej@hej.com",
        "posts": fakeposts,
    }

    return render(request, "social-app/user_profile.html", context)


@login_required
def search_user(request):
    if "SearchQuery" in request.GET:
        # get all users
        # users=User.object.all()
        data = None

        search_query = request.GET.get("SearchQuery")

        # using Query tool to add multiple quries to get data from model
        # based on first name or last name enetered in search box.
        data = User.objects.filter(Q(username__icontains=search_query))

        context = {"data": data}
        print("data", data)

        return render(request, "social-app/search.html", context)
    else:
        return render(request, "social-app/user_profile.html")
        # return HttpResponse("No search query provided.")

    return HttpResponse("Invalid request method.")


@login_required
def temp_profile(request):
    temp_profile = User.objects.get(pk=1)
    print("temp_profile")
    context = {"temp_profile": temp_profile}
    return render(
        request, template_name="social-app/temp_profile.html", context=context
    )


@login_required
def followers(request):
    """Render the search page."""
    return render(request, "social-app/followers.html")


@login_required
def following(request):
    """Render the search page."""
    return render(request, "social-app/following.html")


@login_required
def feed(request):
    """Render the search page."""
    return render(request, "social-app/feed.html")


def register(request):
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
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/feed/")  # Redirect to your homepage or dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "social-app/login.html")


def custom_logout_view(request):
    logout(request)  # Logs out the user
    return redirect("social_app:login")  # Redirect to the homepage (or another page)
