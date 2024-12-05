""" Models for the social_app app """

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Model representing a user profile"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(
        upload_to="profile_pics/", default="../static/img/user-icon.png"
    )

    bio = models.TextField(max_length=500, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.user.username


class UserFollow(models.Model):
    """Model representing a user following another user"""

    # The user who is following
    follower = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )

    # The user who is being followed
    user_being_followed = models.ForeignKey(
        User, related_name="followers", on_delete=models.CASCADE
    )

    objects = models.Manager()

    def __str__(self):
        """String for representing the Follow object"""
        return f"{self.follower} follows {self.user_being_followed}"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {str(self.content)[:30]}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self", related_name="replies", null=True, blank=True, on_delete=models.CASCADE
    )

    objects = models.Manager()

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"

    class Meta:
        ordering = ["created_at"]
