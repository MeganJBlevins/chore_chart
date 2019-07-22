from django import forms
from django.contrib.auth.models import User
from chore_chart.models import Chore
from chore_chart.models import UserProfileInfo

class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = "__all__"
    

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('profile_image',)
