from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
