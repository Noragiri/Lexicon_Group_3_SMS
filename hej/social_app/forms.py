from django import forms
from django.contrib.auth.models import User
from social_app.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")
        """TODO: Check if password == repeat password"""


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("bio",)
