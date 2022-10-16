from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    # author = models.ForeignKey( on_delete=models.CASCADE)
# Create your models here.
