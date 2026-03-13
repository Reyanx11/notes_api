from .models import Notes
from rest_framework import serializers

class NotesSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.HyperlinkedRelatedField(
        view_name = "user-detail",
        read_only = True
    )

    class Meta:
        model = Notes
        fields = ["url", "title", "content", "author", "is_public"]
        extra_kwargs = {
            "url" : {"view_name": "notes-detail"}
        }