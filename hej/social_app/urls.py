""" URL Configuration for social_app app. """

from django.urls import path
from social_app.views import temporary_startpage
from . import views
from social_app.views import temp_profile


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
    
    # Correct URLs for followers and following (make sure they include user_id)
    path("profile/<int:user_id>/followers/", views.followers, name='followers'),
    path("profile/<int:user_id>/following/", views.following, name='following'),

    # Follow user
    path("follow/<int:user_id>/", views.follow_user, name="follow_user"),
    
    # Other paths for search, login, registration, and logout
    path("search/", search_user, name="search_user"),
    path("search/temp/", temp_profile, name="temp_profile"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", custom_logout_view, name="logout"),

    # Temporary path for starting page
    path('temporary_startpage/', temporary_startpage, name='temporary_startpage'),
    path('profile/<int:user_id>/following/', views.following_view, name='following'),
]