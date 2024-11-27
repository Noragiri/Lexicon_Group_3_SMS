""" Views for the social app. """

from django.shortcuts import render, get_object_or_404, redirect
from social_app.models import UserProfile, Post
from django.contrib.auth.models import User
from social_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


app_name = "social_app"

# Create your views here.


def temporary_startpage(request):
    """Render the temporary startpage."""
    return render(request, "social-app/temporary_startpage.html")


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


def followers(request):
    """Render the search page."""
    return render(request, "social-app/followers.html")


def following(request):
    """Render the search page."""
    return render(request, "social-app/following.html")


def search(request):
    """Render the search page."""
    return render(request, "social-app/search.html")


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_picture" in request.FILES:
                profile.profile_picture = request.FILES["profile_picture"]

            profile.save()

            registered = True

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
            return redirect("/")  # Redirect to your homepage or dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "social-app/login.html")


def custom_logout_view(request):
    logout(request)  # Logs out the user
    return redirect("social_app:login")  # Redirect to the homepage (or another page)
