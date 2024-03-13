from django import forms
from .models import SubscriptionPlan


class SubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__' 
        exclude = ('stripe_price_id',)


class SubscriptionPlanEditForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__' 
        widgets = {
            'staged': forms.CheckboxInput(),           
        }
