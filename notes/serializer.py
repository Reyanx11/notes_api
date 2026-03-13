from .models import Notes
from rest_framework import serializers

class NotesSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source = "author.username")

    class Meta:
        model = Notes
        fields = '__all__'