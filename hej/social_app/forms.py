from django import forms
from django.contrib.auth.models import User
from social_app.models import UserProfile


class UserForm(forms.ModelForm):
    """Form for the User model"""

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        """Specify the model and fields to include in the form"""

        model = User
        fields = ("username", "email", "password")
        """TODO: Check if password == repeat password"""


class UserProfileInfoForm(forms.ModelForm):
    """Form for the UserProfile model"""

    class Meta:
        """Specify the model and fields to include in the form"""

        model = UserProfile
        fields = ("bio",)

    def clean_email(self):
        """Validate that the email is unique"""
        email = self.cleaned_data.get("email")
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
