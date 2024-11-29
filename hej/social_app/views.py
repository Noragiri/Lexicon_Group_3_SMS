from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Follow, UserProfile, Post
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import User
from django.shortcuts import render


@login_required
def followers(request, user_id):
    """Render the followers list for a user."""
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    user = User.objects.get(id=user_id)

    # Get all followers of the target user
    followers = Follow.objects.filter(following=user_profile)
    followers_list = [f.follower for f in followers]  # Get the followers

    context = {
        "user_profile": user_profile,
        "followers_list": followers_list,
    }

    return render(request, "social-app/followers.html", context)

# View to show the list of following
@login_required
def following(request, user_id):
    """Render the following list for a user."""
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)

    # Get all users that this user is following
    following = Follow.objects.filter(follower=user_profile)
    following_list = [f.following for f in following]  # Get the following list

    context = {
        "user_profile": user_profile,
        "following_list": following_list,
    }

    return render(request, "social-app/following.html", context)


def followers(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    followers_list = user_profile.followers.all()  # Assuming the relation is set up
    return render(request, 'social-app/followers.html', {
        'user_profile': user_profile,
        'followers_list': followers_list,
    })

def following(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    following_list = user_profile.following.all()  # Assuming the relation is set up
    return render(request, 'social-app/following.html', {
        'user_profile': user_profile,
        'following_list': following_list,
    })

def follow_user(request, user_id):
    """Handle following a user."""
    # Get the user to follow
    user_to_follow = get_object_or_404(User, id=user_id)
    user_profile = request.user.profile  # Get the profile of the logged-in user
    
    # Check if the logged-in user is already following the target user
    if not Follow.objects.filter(follower=user_profile, following=user_to_follow.profile).exists():
        # If not, create a new follow relationship
        Follow.objects.create(follower=user_profile, following=user_to_follow.profile)
        messages.success(request, f"You are now following {user_to_follow.username}")
    else:
        messages.info(request, f"You are already following {user_to_follow.username}")

    return redirect('social_app:user_profile', user_id=user_id)  # Redirect to the user's profile


def user_profile(request, user_id=0):
    """Render the user profile."""
    if user_id == 0:
        context = {
            "username": "Guest",
            "profile_pic": None,
            "about": "This is a guest profile. Log in or specify a user ID to view a profile.",
            "email": "guest@example.com",
            "user_posts": [],
        }
        return render(request, "social-app/user_profile.html", context)

    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    user_posts = Post.objects.filter(user=user).order_by("-created_at")

    context = {
        "user_id": user.id,
        "username": user.username,
        "profile_pic": (
            user_profile.profile_pic.url if user_profile.profile_pic else None
        ),
        "about": user_profile.bio,
        "email": user.email,
        "user_profile": user_profile,
        "user_posts": user_posts,
    }

    return render(request, "social-app/user_profile.html", context)


def user_profile_no_id(request, user_id=0):
    """Render the user profile."""
    fakeposts = [
        {"post_id": 1, "name": "Name Namesson", "date": "2024-12-04", "message": "Oyeah this and that"},
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {"post_id": 2, "name": "John Smith", "date": "2024-12-06", "message": "Yet another post content"},
        {"post_id": 3, "name": "Name Namesson", "date": "2024-12-04", "message": "Oyeah this and that"},
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {"post_id": 4, "name": "John Smith", "date": "2024-12-06", "message": "Yet another post content"},
    ]

    context = {
        "user_id": user_id,
        "username": "Alice",
        "password": "password",
        "profile_pic": "https://www.fillmurray.com/200/300",
        "about": "I am a software engineer.",
        "email": "hej@hej.com",
        "posts": fakeposts,
    }

    return render(request, "social-app/user_profile.html", context)


def search_user(request):
    if "SearchQuery" in request.GET:
        search_query = request.GET.get("SearchQuery")
        data = User.objects.filter(Q(username__icontains=search_query))
        context = {"data": data}
        return render(request, "social-app/search.html", context)
    else:
        return render(request, "social-app/user_profile.html")


def temp_profile(request):
    temp_profile = User.objects.get(pk=1)
    context = {"temp_profile": temp_profile}
    return render(request, "social-app/temp_profile.html", context)


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_picture" in request.FILES:
                profile.profile_picture = request.FILES["profile_picture"]

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "social-app/registration.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "registered": registered,
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  # Redirect to your homepage or dashboard
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "social-app/login.html")


def custom_logout_view(request):
    logout(request)  # Logs out the user
    return redirect("social_app:login")  # Redirect to the login page


def followers(request):
    """Render the followers page (currently placeholder)."""
    return render(request, "social-app/followers.html")


def following(request):
    """Render the following page (currently placeholder)."""
    return render(request, "social-app/following.html")

def temporary_startpage(request):
    return render(request, 'social-app/temporary_startpage.html')