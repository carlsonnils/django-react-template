from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Topic, Post
from .serializers import TopicSerializer, PostSerializer


@api_view(['GET'])
def admin(request):
    # TODO: check request.user
    # TODO: check reqeust.auth
    pass


@api_view(['GET'])
def all_topics_posts(request):
    # TODO: check request.user
    # TODO: check reqeust.auth
    topic_queryset = Topic.objects.all()
    topic_data = TopicSerializer(topic_queryset)

    post_queryset = Post.objects.all()
    post_data = PostSerializer(post_queryset)
    
    return Response({'Topics': topic_data, 'Posts': post_data}, status=status.HTTP_OK_200)