from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from app.routers import router
from app.api_views import RegisterUsers, ImpactPost
from app.views import index

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path(
        'api/auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path('api/auth/register/', RegisterUsers.as_view(), name="register"),
    path('api/impact/post/', ImpactPost.as_view(), name="impact"),
]
