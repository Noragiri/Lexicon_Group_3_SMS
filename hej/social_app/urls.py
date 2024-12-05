""" URL Configuration for social_app app. """

from django.urls import path
from social_app.views import (
    user_profile,
    register,
    login_view,
    custom_logout_view,
    search_user,
    feed,
    view_post,
    follow_user,
    followers,
    following,
)


app_name = "social_app"


urlpatterns = [
    path("", login_view, name="login"),
    path("register/", register, name="register"),
    path("feed/", feed, name="feed"),
    path("user_profile/<int:user_id>/", user_profile, name="user_profile"),
    path("profile/", user_profile, name="my_user_profile"),
    path("follow/<int:user_id>/", follow_user, name="follow_user"),
    path("followers/", followers, name="my_followers"),
    path("following/", following, name="my_following"),
    path("search/", search_user, name="search_user"),
    path("logout/", custom_logout_view, name="logout"),
    path("post/<int:post_id>/", view_post, name="view_post"),
]

#    path("follow/<int:user_id>/", toggle_follow, name="toggle_follow"),
