from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User)

    @property
    def likes_quantity(self):
        return len(self.likes.all())

    def __str__(self):
        return '{0}... ({1} likes)'.format(self.text[:20], self.likes_quantity)
