from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "masterdata/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Hello shepherd",
            'message' : "Hello shepherd!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )


def about(request):
    return render(
        request,
        "masterdata/about.html",
        {
            'title' : "About shepherd",
            'content' : "Example app page for shepherd."
        }
    )