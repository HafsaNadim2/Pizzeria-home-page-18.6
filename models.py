from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(primary_key=True,max_length=20)
   
    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE)
    name = models.CharField(primary_key=True, max_length=40)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return str (self.name)[:50] + "..."
