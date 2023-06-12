from rest_framework import routers
from ideas.viewsets import TopicViewSet, PostViewSet
from ideas.views import all_topics_posts
# TODO: add in posts viewset

router = routers.SimpleRouter()
router.register(r'all_topics_posts', all_topics_posts)
router.register(r'topic', TopicViewSet) # TODO: update to pass the primary key in the url
router.register(r'post', PostViewSet) # TODO: update to pass the primary key in the url