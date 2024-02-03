from . import views
from django.urls import path

urlpatterns = [
    path('', views.NewsList.as_view(), name="home"),
    path('<slug:slug>/', views.news_detail, name="news_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]