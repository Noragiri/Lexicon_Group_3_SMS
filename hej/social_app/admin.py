from django.contrib import admin
from social_app.models import UserProfile, Post, UserFollow, Comment

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserFollow)
admin.site.register(Post)
admin.site.register(Comment)
