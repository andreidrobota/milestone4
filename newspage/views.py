from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import News, Comment
from .forms import CommentForm

# Create your views here.


class NewsList(generic.ListView):
    queryset = News.objects.filter(status=1)
    template_name = "newspage/index.html"
    paginate_by = 3


def news_detail(request, slug):
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
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
         },
         )


def edit_comment(request, slug, comment_id):
    """
    comment editing
    """
    if request.method == "POST":

        queryset = News.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been successfully updated!')
        else:
            messages.add_message(
                request, messages.ERROR,
                "An error occured updating your comment!")

    return HttpResponseRedirect(reverse('news_detail', args=[slug]))


def delete_comment(request, slug, comment_id):
    """
    comment deleting
    """

    queryset = News.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been successfully deleted!')
    else:
        messages.add_message(
                request, messages.ERROR,
                "An error occured deleting your comment!")

    return HttpResponseRedirect(reverse('news_detail', args=[slug]))
