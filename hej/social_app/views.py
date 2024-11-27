""" Views for the social app. """

from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import UserProfile, Post
from django.contrib.auth.models import User
from django.db.models import Q   


app_name = "social_app"

# Create your views here.


def temporary_startpage(request):
    """Render the temporary startpage."""
    return render(request, "social-app/temporary_startpage.html")


def user_profile(request, user_id=0):
    """Render the user profile."""

    # If no user_id is provided, show a default user profile (or a placeholder for now)
    if user_id == 0:
        context = {
            "username": "Guest",
            "profile_pic": None,
            "about": "This is a guest profile. Log in or specify a user ID to view a profile.",
            "email": "guest@example.com",
            "user_posts": [],
        }
        return render(request, "social-app/user_profile.html", context)

    # Fetch the user and their profile by ID
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

    # Fake data just added to display something

    fakeposts = [
        {
            "post_id": 1,
            "name": "Name Namesson",
            "date": "2024-12-04",
            "message": "Oyeah this and that",
        },
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {
            "post_id": 2,
            "name": "John Smith",
            "date": "2024-12-06",
            "message": "Yet another post content",
        },
        {
            "post_id": 3,
            "name": "Name Namesson",
            "date": "2024-12-04",
            "message": "Oyeah this and that",
        },
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {
            "post_id": 4,
            "name": "John Smith",
            "date": "2024-12-06",
            "message": "Yet another post content",
        },
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


def user_profile_no_id(request,user_id=0):
    """Render the user profile."""

    # Fake data just added to display something

    fakeposts = [
        {
            "post_id": 1,
            "name": "Name Namesson",
            "date": "2024-12-04",
            "message": "Oyeah this and that",
        },
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {
            "post_id": 2,
            "name": "John Smith",
            "date": "2024-12-06",
            "message": "Yet another post content",
        },
        {
            "post_id": 3,
            "name": "Name Namesson",
            "date": "2024-12-04",
            "message": "Oyeah this and that",
        },
        {"name": "Jane Doe", "date": "2024-12-05", "message": "Another post content"},
        {
            "post_id": 4,
            "name": "John Smith",
            "date": "2024-12-06",
            "message": "Yet another post content",
        },
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



#view to search user 

def search_user(request):
      if 'SearchQuery' in request.GET:
       # get all users
        #users=User.object.all()
        data=None


        search_query=request.GET.get('SearchQuery')

        #using Query tool to add multiple quries to get data from model 
        # based on first name or last name enetered in search box.
        multiple_q=Q(Q(first_name__icontains=search_query) | Q(username__icontains=search_query)| Q(last_name__icontains=search_query))
        data=User.objects.filter(multiple_q)
    
        context={'data':data}
        print('data',data)


        return render(request, "social-app/search.html", context)
      else:
            return render(request, "social-app/user_profile.html"   )
               #return HttpResponse("No search query provided.")

      return HttpResponse("Invalid request method.")

#view to search user 

def temp_profile(request):
    temp_profile=User.objects.get(pk=1)
    print('temp_profile')
    context={'temp_profile':temp_profile}
    return render(request, template_name='social-app/temp_profile.html',context=context)


def followers(request):
    """Render the search page."""
    return render(request, "social-app/followers.html")


def following(request):
    """Render the search page."""
    return render(request, "social-app/following.html")




