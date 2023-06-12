from rest_framework import routers
from ideas.viewsets import TopicViewSet
# TODO: add in posts viewset

router = routers.SimpleRouter()
router.register(r'topic', TopicViewSet) # TODO: update to pass the primary key in the url
# TODO: register the PostViewSet to the router