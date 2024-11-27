""" Views for the social app. """

from django.shortcuts import render , HttpResponse
from django.db.models import Q   
from django.contrib.auth.models import User



app_name = "social_app"

# Create your views here.


def user_profile(request, user_id=0):
    """Render the user profile."""
    """ Make database request for user with id passed in """

    context = {
        "user_id": user_id,
        "username": "Alice",
        "password": "password",
        "profile_pic": "https://www.fillmurray.com/200/300",
        "about": "I am a software engineer.",
        "email": "hej@hej.com",
    }

   
    return render(request, "social-app/user_profile.html", context)


def user_profile_no_id(request,user_id=0):
    """Render the user profile."""
    """ Make database request for user with id passed in """
    context = {
        "user_id": user_id,
        "username": "Alice",
        "password": "password",
        "profile_pic": "https://www.fillmurray.com/200/300",
        "about": "I am a software engineer.",
        "email": "hej@hej.com",
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


  
