from django.db import models # a module called models is being imported for us, and we're being invited to create models of our own

# Create your models here.
class Pizza(models.Model): # this has created a class called Pizza and lets us add fields such as name
    name = models.CharField(primary_key=True,max_length=20) # CharField lets you store a small amount of text, such as a name, a title, or a city 
   
    def __str__(self): # this returns a string store in the name attribute
        return self.name

class Topping(models.Model): # this creates a Topping class and lets us include fields such as pizza and name
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE) # ForeignKey is a column that provides a link between data in two tables
    name = models.CharField(primary_key=True, max_length=40) # CharField stores a text

    class Meta: # this allows us to set a special attribute telling Django to use Toppings when it needs to refer to more than one topping
        verbose_name_plural = 'toppings'

    def __str__(self): # the string method tells Django which info. to show when it refers to individual toppings
        return str (self.name)[:50] 
