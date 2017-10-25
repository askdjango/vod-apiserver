from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]

