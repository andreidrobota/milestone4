from django.contrib import admin
from .models import AboutApp
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(AboutApp)
class AboutAppAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)