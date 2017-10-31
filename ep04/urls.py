from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'post', views.PostViewSet)  # 2개의 URL을 처리하는 뷰함수를 만들어서 등록
# router.urls

urlpatterns = [
    url(r'', include(router.urls)),  # /ep04/post/1/
]

