from django.shortcuts import render #  file just imports the render() function, which renders the response based on the data provided by views

def index(request):
    """The home page for Pizzeria."""
    return render(request, 'pizzas/index.html') # The render() function here uses two arguments—the original request object and a template it can use to build the page
