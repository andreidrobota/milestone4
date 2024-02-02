from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import News
from .forms import CommentForm

# Create your views here.

class NewsList(generic.ListView):
    queryset = News.objects.filter(status=1)
    template_name = "newspage/index.html"
    paginate_by = 3


def news_detail(request,slug):
    queryset = News.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-added_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment waiting for approval'
            )

    comment_form = CommentForm()


    return render(
        request, 
        "newspage/news_detail.html",
         {"post": post,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
         )