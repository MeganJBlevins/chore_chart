from rest_framework import viewsets
from .models import UserProfileInfo
from .serializers import UserProfileInfoSerializer


class UserProfileInfoViewSet(viewsets.ModelViewSet):
    queryset = UserProfileInfo.objects.all()
    serializer_class = UserProfileInfoSerializer