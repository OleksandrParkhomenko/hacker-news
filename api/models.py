from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    author = models.CharField(max_length=200, default="anonymous")
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    upvotes_amount = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, default=None, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.CharField(max_length=200, default="anonymous")
    content = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return "Comment from {} by {}".format(self.created_date, self.author)
