""" Views for the social app. """

from django.shortcuts import render


app_name = "social_app"

# Create your views here.


def temporary_startpage(request):
    """Render the temporary startpage."""
    return render(request, "social-app/temporary_startpage.html")


def user_profile(request, user_id=0):
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
