from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework.decorators import action
from . import models 
from . import serializers 

class PostViewset(viewsets.ModelViewSet):
	queryset = models.Post.objects.all()
	serializer_class = serializers.PostSerializer 

	@action(detail=True, methods=['POST'], name='upvote_post')
	def upvote_post(self, request, pk=None):
		post = models.Post.objects.get(pk=pk)
		post.upvotes_amount += 1
		post.save()
		serializer = self.get_serializer(post, many=False)
		return Response(serializer.data)

	@action(detail=False, methods=['POST'], name='reset_upvotes')
	def reset_upvotes(self, request):
		posts = models.Post.objects.all()
		posts.update(upvotes_amount=models.Post.upvotes_amount.field.default)
		serializer = self.get_serializer(posts, many=True)
		return Response(serializer.data)


class CommentViewset(viewsets.ModelViewSet):
	queryset = models.Comment.objects.all()
	serializer_class = serializers.CommentSerializer 


