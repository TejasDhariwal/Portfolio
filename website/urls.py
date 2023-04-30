from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"), 
    path('textutils', views.textutils, name="textutils"),
    path('gym', views.gym, name="gym"),
]
