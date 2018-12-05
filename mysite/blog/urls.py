from django.urls import path

from . import views

urlpatterns = [
   path('', views.hello, name='hello'), 
   path('hello1', views.hello1, name='hello') 
]
