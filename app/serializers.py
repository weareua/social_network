from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'posts']


class PostCreateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ['text', ]


class PostGeneralSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'likes']
