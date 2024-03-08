from django import forms
from .models import SubscriptionPlan

class SubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__' 

class SimpleSubscriptionPlanEditForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__' 
        widgets = {
            'staged': forms.CheckboxInput(),           
        }
