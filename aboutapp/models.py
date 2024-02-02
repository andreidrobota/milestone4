from django.db import models

# Create your models here.

class AboutApp(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    renewed_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title