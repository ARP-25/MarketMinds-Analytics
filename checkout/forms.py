from django import forms
from .models import ActiveSubscription

class ActiveSubscriptionForm(forms.ModelForm):
    """
    Form for user subscription information.

    Fields:
    - full_name: CharField for user's full name.
    - email: EmailField for user's email address.
    - phone_number: CharField for user's phone number.
    - country: CharField for user's country.
    - postcode: CharField for user's postal code.
    - town_or_city: CharField for user's town or city.
    - street_address1: CharField for user's street address (line 1).
    - street_address2: CharField for user's street address (line 2).
    - county: CharField for user's county.

    The form initializes with placeholder text and styling for a Stripe-style input.
    """
    class Meta:
        model = ActiveSubscription
        fields = ['full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county']

    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    country = forms.CharField(max_length=40, required=False)
    postcode = forms.CharField(max_length=20, required=False)
    town_or_city = forms.CharField(max_length=40, required=False)
    street_address1 = forms.CharField(max_length=80, required=False)
    street_address2 = forms.CharField(max_length=80, required=False)
    county = forms.CharField(max_length=80, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False