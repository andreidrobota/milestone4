from django.shortcuts import render
from .models import AboutApp

# Create your views here.

def about_us(request):
    """
    Renders the About page
    """
    about = AboutApp.objects.all().order_by('-renewed_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
