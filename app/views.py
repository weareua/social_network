from django.shortcuts import render

from app.models import Post


def index(request):
    data = Post.objects.all().order_by('-created_date')
    return render(request, 'app/index.html', {"data": data})
