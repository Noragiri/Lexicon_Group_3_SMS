from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Post
from django.contrib.auth.models import User

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
    user_posts = Post.objects.filter(user=user).order_by('-created_at')

    context = {
        "user_id": user.id,
        "username": user.username,
        "profile_pic": user_profile.profile_pic.url if user_profile.profile_pic else None,
        "about": user_profile.bio,
        "email": user.email,
        "user_profile": user_profile,
        "user_posts": user_posts,
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
