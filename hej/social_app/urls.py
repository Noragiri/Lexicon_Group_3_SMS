""" URL Configuration for social_app app. """

from django.urls import path
from social_app.views import user_profile

app_name = "social_app"

urlpatterns = [
    path("user_profile/", user_profile, name="user_profile_no_id"),
    path("user_profile/<int:user_id>/", user_profile, name="user_profile"),
]
