from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/$', views.PostListAPIView.as_view()),
]

