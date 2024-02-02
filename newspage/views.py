from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import News

# Create your views here.

class NewsList(generic.ListView):
    queryset = News.objects.filter(status=1)
    template_name = "newspage/index.html"
    paginate_by = 3


def news_detail(request,slug):
    queryset = News.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(request, "newspage/news_detail.html", {"post": post},)