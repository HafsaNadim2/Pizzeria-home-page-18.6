from django.contrib import admin

# Register your models here.
from pizzas.models import Pizza, Topping # This code imports the models we want to register, Pizza and Topping

admin.site.register(Pizza) # to tell Django to manage our model through the admin site
admin.site.register(Topping) # to tell Django to manage our model through the admin site 


