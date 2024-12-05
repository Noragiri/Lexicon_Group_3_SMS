import os
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hej.settings")

import django

django.setup()
# Fake pop script

import random
from social_app.models import User, UserProfile, Post, UserFollow, Comment
from faker import Faker


fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        # Create fake data for entry
        fake_username = fakegen.user_name()
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        print("Create new User entry")
        user, created = User.objects.get_or_create(
            username=fake_username,
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake_email,
        )
        if created:
            user.set_password("password")  # Set a default password
            user.save()

        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            user_profile.profile_pic = fakegen.image_url()
            user_profile.bio = fakegen.text()
            user_profile.save()

        print("Create new Post entry")
        post = Post.objects.get_or_create(user=user, content=fakegen.text())[0]

        # Create new UserFollow entry
        # user_follow = UserFollow.objects.get_or_create(follower=user, following=user)[0]

        print("Create new Comment entry")
        comment = Comment.objects.get_or_create(
            user=user, post=post, content=fakegen.text()
        )


if __name__ == "__main__":
    print("populating script!")
    populate(999)
    print("populating complete")
