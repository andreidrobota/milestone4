from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about'),
    path('submit-work-request/', views.submit_work_request, name='submit_work_request'),
]