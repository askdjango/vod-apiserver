from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list = PostViewSet.as_view({
    'get': 'list',
})

