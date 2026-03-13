from .models import Notes
from .serializer import NotesSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

class NoteList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class NoteDetails(generics.RetrieveUpdateDestroyAPIView):

    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    