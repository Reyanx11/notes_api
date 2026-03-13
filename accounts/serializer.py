from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ["url", "username"]

        extra_kwargs = {
            "url": {"view_name": "user_detail"}
        }

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    
