from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=280)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    people = models.JSONField(default=list)
    objects = models.Manager()


class HashTag(models.Model):
    hashtag = models.CharField(max_length=280)
    tag = models.CharField(max_length=139, default='')
    tweet = models.ManyToManyField(Tweet)
    objects = models.Manager()





