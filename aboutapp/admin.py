from django.contrib import admin
from .models import AboutApp, WorkRequest
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(AboutApp)
class AboutAppAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(WorkRequest)
class WorkRequestAdmin(admin.ModelAdmin):

    list_display = ('name', 'read',)