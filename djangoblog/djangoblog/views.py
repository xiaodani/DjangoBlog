
"""

function which is called when user access url

"""

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  # return HttpResponse("This is an Home Page response")
    return render(request, 'home.html')

def about(request):
  # return HttpResponse("This is an about response")
    return render(request, 'about.html')