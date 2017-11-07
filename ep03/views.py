from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .pagination import PostPageNumberPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPageNumberPagination


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

