import os
import lorem
import random
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from app.models import Post


class Command(BaseCommand):
    help = 'Populates db with users, posts and likes'

    def handle(self, *args, **options):
        try:
            users = list()
            # create users
            for user_iteration in list(
                    range(0, int(os.getenv("NUMBER_OF_USERS_TO_POPULATE")))):
                name = "John{0}".format(datetime.now().microsecond)

                user = User.objects.create_user(
                    username=name, password="qwerty", email="doe@example.com"
                )
                users.append(user)
                # create posts
                for post_teration in list(
                        range(0, int(os.getenv("MAX_POSTS_PER_USER")))):
                    Post.objects.create(
                        author=user, text=lorem.paragraph())
            # like posts by newly created users pool
            for user in users:
                for like_iteration in list(
                        range(0, int(os.getenv("MAX_LIKES_PER_USER")))):
                    posts = Post.objects.exclude(likes=user)
                    post = random.choice(posts)
                    post.likes.add(user)
                    post.save()
        except Exception as e:
            raise CommandError(
                'Error was triggered during database population: {0}'.format(str(e)))  # noqa

        self.stdout.write(self.style.SUCCESS(
            'Database was successfully populated'))
