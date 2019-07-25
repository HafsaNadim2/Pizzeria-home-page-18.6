from django.shortcuts import render

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html') # The render() function here uses two arguments—the original request object and a template it can use to build the page
