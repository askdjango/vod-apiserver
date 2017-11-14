from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .permissions import IsAuthorUpdateOrReadonly
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorUpdateOrReadonly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            ip=self.request.META['REMOTE_ADDR'])

