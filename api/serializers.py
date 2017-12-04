from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from api.models import Post


class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author_username', 'message', 'photo']
