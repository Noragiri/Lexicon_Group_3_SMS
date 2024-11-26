""" Views for the social app. """

from django.shortcuts import render


app_name = "social_app"

# Create your views here.


def user_profile(request, user_id=0):
    """Render the user profile."""
    """ Make database request for user with id passed in """

    context = {
        "user_id": user_id,
        "username": "Alice",
        "password": "password",
        "profile_pic": "https://www.fillmurray.com/200/300",
        "about": "I am a software engineer.",
        "email": "hej@hej.com",
    }

    return render(request, "social-app/user_profile.html", context)


def user_profile_no_id(request, user_id=0):
    """Render the user profile."""
    """ Make database request for user with id passed in """
    context = {
        "user_id": user_id,
        "username": "Alice",
        "password": "password",
        "profile_pic": "https://www.fillmurray.com/200/300",
        "about": "I am a software engineer.",
        "email": "hej@hej.com",
    }

    return render(request, "social-app/user_profile.html", context)
