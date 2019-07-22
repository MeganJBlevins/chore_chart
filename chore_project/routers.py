from rest_framework import routers
from chore_chart.viewsets import UserProfileInfoViewSet

router = routers.DefaultRouter()
router.register(r'UserProfileInfo', UserProfileInfoViewSet)