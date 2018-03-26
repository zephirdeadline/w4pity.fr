from django.db import models

# Create your models here.


class Site(models.Model):
    title = models.CharField(max_length=64)
    subTitle = models.CharField(max_length=64)
    footer = models.CharField(max_length=64)
    linkedin = models.CharField(max_length=64)
    cv = models.CharField(max_length=64)
    git = models.CharField(max_length=64)
    about = models.TextField(max_length=64)
    pseudo = models.CharField(max_length=64)


class Post(models.Model):
    title = models.CharField(max_length=128)
    subTitle = models.CharField(max_length=512)
    date = models.DateField()
    content = models.TextField(blank=True, null=True)
    isProject = models.BooleanField()
    img = models.ImageField(upload_to='static/upload/')
    tags = models.CharField(max_length=128, blank=True, null=True)


class File(models.Model):
    path = models.FileField(upload_to='static/upload/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
