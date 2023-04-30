from django.shortcuts import render, HttpResponse
from .models import UserInfo
from django.contrib import messages
from datetime import date

# Create your views here.
def home(request):
    if request.method == "POST":
        # Extracting the user information
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Making the object of the model using the information of the user
        user_information = UserInfo(user_name=name, user_email=email, user_message=message, date=date.today())

        # Saving the information of the user in the admin site
        user_information.save()


    return render(request, 'home.html')

def textutils(request):
    return render(request, "textutils.html")

def gym(request):
    return render(request, "gym.html")
