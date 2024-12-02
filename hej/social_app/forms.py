from django import forms
from django.contrib.auth.models import User
from social_app.models import UserProfile, Comment


class UserForm(forms.ModelForm):
    """Form for the User model"""

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
        label="Password",
        help_text="Enter your password.",
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
        label="Confirm Password",
        help_text="Re-enter your password for confirmation.",
    )

    class Meta:
        """Specify the model and fields to include in the form"""

        model = User
        fields = ("username", "email", "password")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
        }

    def clean(self):
        """Override clean method to validate password match"""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")

        return cleaned_data


class UserProfileInfoForm(forms.ModelForm):
    """Form for the UserProfile model"""

    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Tell us about yourself",
                "rows": 3,
                "maxlength": 500,
            }
        ),
        required=False,  # Optional field
        label="Describe yourself",
    )

    profile_pic = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control",
                "accept": "image/*",  # Accept only image files
            }
        ),
        required=False,  # Optional field
        label="Profile Picture",
    )

    class Meta:
        """Specify the model and fields to include in the form"""

        model = UserProfile
        fields = ("bio", "profile_pic")


class CommentForm(forms.ModelForm):
    """Form for adding comments to a post"""

    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Write a comment..."}),
        label="",
    )

    class Meta:
        model = Comment
        fields = ("content",)
