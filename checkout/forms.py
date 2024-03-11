from django import forms
from .models import ActiveSubscription

class ActiveSubscriptionForm(forms.ModelForm):
    """
    Form for user subscription information.

    Fields:
    - full_name: CharField for user's full name.
    - email: EmailField for user's email address.

    The form initializes with placeholder text and styling for a Stripe-style input.
    """
    class Meta:
        model = ActiveSubscription
        fields = ['full_name', 'email']

    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
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


    