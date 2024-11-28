from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Model representing a user profile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pics/", default="static/img/user-icon.jpg"
    )
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.content[:30]}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"
