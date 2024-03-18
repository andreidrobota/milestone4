from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class News(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name="news_posts"
    )
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    posting_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    teaser = models.TextField(blank=True)

    class Meta:
        ordering = ["-posting_date"]

    def __str__(self):
        return f"{self.title} | created by {self.author}"



class Comment(models.Model):
    post = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["added_on"]

    def __str__(self):
        return f"Comment with the content of '{self.body}' " \
                f"written by {self.author}"