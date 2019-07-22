from rest_framework import serializers
from .models import UserProfileInfo


class UserProfileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = '__all__'
