from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # /ep04/post/ => list() 함수가 호출
    # /ep04/post/public_list/ => public_list() 함수가 호출

    @list_route()
    def public_list(self, request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # /ep04/post/10/ => retrieve() 함수가 호출
    # /ep04/post/10/set_public/ => set_public() 함수가 호출

    @detail_route(methods=['patch'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

