from django.contrib import admin
from chore_chart.models import UserProfileInfo
from chore_chart.models import Chore

admin.site.register(Chore)
admin.site.register(UserProfileInfo)