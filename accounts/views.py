from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import generics

class userList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
