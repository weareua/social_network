from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from app.utils import check_email
from app.models import Post


class RegisterUsers(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email are required to register a user"  # noqa
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        email_valid = check_email(email)
        if email_valid:
            User.objects.create_user(
                username=username, password=password, email=email
            )
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "email is not valid"},
                status=status.HTTP_406_NOT_ACCEPTABLE)


class ImpactPost(APIView):

    def post(self, request, *args, **kwargs):
        post_id = request.data.get("post_id", "")
        if not post_id:
            return Response(
                data={
                    "message": "post id is required to make an impact"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            try:
                post = Post.objects.get(pk=post_id)
                user = request.user
                action = 'liked'
                if user in post.likes.all():
                    post.likes.remove(user)
                    action = 'unliked'
                else:
                    post.likes.add(user)

                user.save()
                message = "{0} {1} {2} post created by {3}".format(
                    user.username, action, post, post.author)
                return Response({"message": message},
                                status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response(
                    data={
                        "message": "post with provided id is not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
