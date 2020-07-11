from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=200)
	link = models.URLField(max_length=200)
	author = models.CharField(max_length=200)
	#author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#created_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	created_date = models.DateTimeField(default=timezone.now, blank=True)
	upvotes_amount = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	content = models.TextField(null=True, blank=True)
	#created_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	created_date = models.DateTimeField(default=timezone.now, blank=True)


	def __str__(self):
		return self.title

