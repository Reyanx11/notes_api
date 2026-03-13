from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notes.views import NotesViewSet, api_root
from accounts.views import UserViewSet

router = DefaultRouter()
router.register(r'notes', NotesViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]