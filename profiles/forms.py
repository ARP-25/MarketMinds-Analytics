from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Fields:
        email (EmailField): The user's email address.

    The form sets the 'stripe-style-input' class for styling purposes.
    """
    class Meta:
        model = UserProfile
        fields = ['email',]
        widgets = {
            field: forms.TextInput(attrs={'class': 'stripe-style-input'})
            for field in fields
        }
