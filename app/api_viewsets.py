from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.serializers import (UserSerializer,
                             PostCreateSerializer, PostGeneralSerializer)
from app.models import Post


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return PostGeneralSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
