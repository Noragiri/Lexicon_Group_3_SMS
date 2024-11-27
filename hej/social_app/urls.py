""" URL Configuration for social_app app. """

from django.urls import path
from social_app.views import (
    user_profile,
    followers,
    following,
    temporary_startpage,
    register,
    login_view,
    custom_logout_view,
    search_user,
    temp_profile,
)

app_name = "social_app"

# Do we need this?
# path("user_profile/", user_profile, name="user_profile_my_profile"),
# path("user_profile/<int:user_id>/", user_profile, name="user_profile"),

urlpatterns = [
    path("", temporary_startpage, name="home"),
    path("profile/", user_profile, name="user_profile"),
    path("user_profile/<int:user_id>/", user_profile, name="user_profile"),
    path("followers/", followers, name="followers"),
    path("following/", following, name="following"),
    path("search/", search_user, name="search_user"),
    path("search/temp/", temp_profile, name="temp_profile"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", custom_logout_view, name="logout"),
]
