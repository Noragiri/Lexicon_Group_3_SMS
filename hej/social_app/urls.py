""" URL Configuration for social_app app. """

from django.urls import path, include
from social_app.views import (
    user_profile,
    followers,
    following,
    register,
    login_view,
    custom_logout_view,
    search_user,
    feed,
    view_post,
    follow_user,
)


app_name = "social_app"

# Do we need this?
# path("user_profile/", user_profile, name="user_profile_my_profile"),
# path("user_profile/<int:user_id>/", user_profile, name="user_profile"),
#    path("", temporary_startpage, name="home"),
# path("user_profile/<int:user_id>/", user_profile, name="user_profile"),


urlpatterns = [
    path("", login_view, name="login"),
    path("register/", register, name="register"),
    path("feed/", feed, name="feed"),
    path("user_profile/<int:user_id>/", user_profile, name="user_profile"),
    path("profile/", user_profile, name="my_user_profile"),
    path("profile/<int:user_id>/followers/", followers, name="followers"),
    path("profile/<int:user_id>/following/", following, name="following"),
    path("follow/<int:user_id>/", follow_user, name="follow_user"),
    path("search/", search_user, name="search_user"),
    path("logout/", custom_logout_view, name="logout"),
    path("post/<int:post_id>/", view_post, name="view_post"),
]
