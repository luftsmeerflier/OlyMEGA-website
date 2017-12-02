import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     topic = models.CharField(max_length=200)
#     preview = models.CharField(max_length=200, default="")
#     text = models.TextField()
#     created_date=models.DateTimeField(default=timezone.now)
#     published_date=models.DateTimeField(blank=True, null=True)
#
#     # def get_color(self):
    #     colors = {"news":"pink", "events":"gren", "join":"orn"}
    #
    # Post.get_color.color.news

    # 
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
    #
    # def __str__(self):
    #     return self.title
