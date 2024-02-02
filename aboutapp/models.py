from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AboutApp(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    renewed_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="editor", null=True
    )

    def __str__(self):
        return self.title