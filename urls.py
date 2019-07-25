from django.urls import path, include #The first two lines import the functions and modules that manage URLs for the project and admin site 
from django.contrib import admin

urlpatterns = [ # urlpatterns variable includes sets of URLs from the apps in the project
    path('admin/', admin.site.urls), # code includes the module admin.site.urls, which defines all the URLs that can be requested from the admin site
    path('', include('pizzas.urls')), # namespace argument allows us to distinguish meals’s URLs from other URLs that might appear in the project
]
