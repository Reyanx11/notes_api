from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Notes
from .serializer import NotesSerializer
from .permissions import IsOwnerOrReadOnly


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "notes": reverse("notes-list", request=request, format=format),
        "users": reverse("user-list", request=request, format=format),
    })