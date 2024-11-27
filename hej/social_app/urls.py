""" URL Configuration for social_app app. """

from django.urls import path
from social_app.views import (
    user_profile,
    search,
    followers,
    following,
    temporary_startpage,
)

app_name = "social_app"

urlpatterns = [
    path("profile/", user_profile, name="user_profile"),
    path("user_profile/<int:user_id>/", user_profile, name="user_profile"),
    path("followers/", followers, name="followers"),
    path("following/", following, name="following"),
    path("search/", search, name="search"),
]
