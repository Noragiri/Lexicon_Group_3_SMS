from django import forms
from django.contrib.auth.models import User
from social_app.models import UserProfile, Comment


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


class CommentForm(forms.ModelForm):
    """Form for adding comments to a post"""

    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Write a comment..."}),
        label="",
    )

    class Meta:
        model = Comment
        fields = ("content",)
