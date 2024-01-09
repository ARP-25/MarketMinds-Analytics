from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Fields:
    - birth_date: DateField for user's birth date.
    - full_name: CharField for user's full name.
    - email: EmailField for user's email address.
    - phone_number: CharField for user's phone number.
    - country: CharField for user's country.
    - postcode: CharField for user's postal code.
    - town_or_city: CharField for user's town or city.
    - street_address1: CharField for user's street address (line 1).
    - street_address2: CharField for user's street address (line 2).
    - county: CharField for user's county.
    - bio: TextField for user's bio or description.

    The form sets the 'stripe-style-input' class for styling purposes.
    """
    class Meta:
        model = UserProfile
        fields = ['birth_date', 'full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county', 'bio']
        widgets = {
            field: forms.TextInput(attrs={'class': 'stripe-style-input'})
            for field in fields
        }
