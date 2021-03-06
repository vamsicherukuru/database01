from ChristKart.models import Registration
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = Registration
        fields = ('age','gender','profession','location')
