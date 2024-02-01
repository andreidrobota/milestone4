from django.contrib import admin
from .models import News, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'posting_date')
    search_fields = ['title']
    list_filter = ('status','posting_date',)
    prepopulated_field = {'slug': ('title',)}
    summernote_dields = ('content',)


# Register your models here.
admin.site.register(Comment)