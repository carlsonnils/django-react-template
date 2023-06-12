from django.urls import path, re_path
from .views import all_topics_posts

urlpatterns = [
    path('', all_topics_posts),
]