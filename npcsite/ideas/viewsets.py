from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Topic, Post
from .serializers import TopicSerializer, PostSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    This is the  view """
    queryset = Topic.objects.all()  # TODO: query only logged in user Topics
    serializer_class = TopicSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # TODO: query only logged in user Posts
    serializer_class = PostSerializer