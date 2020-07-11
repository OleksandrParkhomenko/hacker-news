from rest_framework import viewsets 
from . import models 
from . import serializers 

class PostViewset(viewsets.ModelViewSet):
	queryset = models.Post.objects.all()
	serializer_class = serializers.PostSerializer 

class CommentViewset(viewsets.ModelViewSet):
	queryset = models.Comment.objects.all()
	serializer_class = serializers.CommentSerializer 