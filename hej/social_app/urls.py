""" URL Configuration for social_app app. """

from django.urls import path
from social_app.views import user_profile,user_profile_no_id,search_user,temp_profile
from . import views

app_name = "social_app"

# urlpatterns = [
#     path("user_profile/", user_profile, name="user_profile_no_id"),
#     path("user_profile/<int:user_id>/", user_profile, name="user_profile"),
#     path("", serach_user, name="serach_user"),
#     path("temp/", temp_profile, name="temp_profile"),


# ]

urlpatterns = [
    #path("user_profile/", views.user_profile, name="user_profile_no_id"),
    path("", views.user_profile_no_id, name="user_profile_no_id"),

    path("user_profile/<int:user_id>/", user_profile, name="user_profile"),
    path("search/", views.search_user, name="search_user"),
    path("search/temp/", views.temp_profile, name="temp_profile"),


]


