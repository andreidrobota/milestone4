from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import AboutApp, WorkRequest
from .forms import WorkRequestForm

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


def submit_work_request(request):
    """
    Work with us form
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        about_me = request.POST.get('about_me')
        why_us = request.POST.get('why_us')

        if name and email and about_me and why_us:
            work_request = WorkRequest(
                name=name, email=email, about_me=about_me, why_us=why_us)
            work_request.save()

            messages.success(request, 'Form submitted succesfully!')
            return HttpResponseRedirect(reverse('about'))
        else:
            return HttpResponseRedirect(reverse('about'))
            messages.error(
                    request, 'Form submission failed, '
                    'please provide valid information!')

    return HttpResponseRedirect(reverse('about'))
