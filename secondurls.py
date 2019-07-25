"""Defines URL patterns for pizzas.""" #  we add a docstring to make it clear, which urls.py we’re working in at the beginning of the file

from django.urls import path # this imports the url function, which is needed when mapping URLs to views

from . import views # the dot tells Python to import views from the same directory as the current urls.py module

app_name = 'pizzas' # need this or will not work in Django 2.2
urlpatterns = [ # The variable urlpatterns in this module is a list of individual pages that can be requested from the pizzas app
    # Home page
    path('', views.index, name='index'), # In its entirety, this expression tells Python to look for a URL with nothing between the beginning and end of the URL
#  the name index provides a link to the home page so we’ll use this name instead of writing out a URL
  ]
