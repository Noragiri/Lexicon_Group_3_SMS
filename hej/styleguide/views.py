""" Views for the styleguide app. """

from django.shortcuts import render


# Create your views here.
def styleguide(request):
    """Render the styleguide."""
    return render(request, "styleguide/styleguide.html")
