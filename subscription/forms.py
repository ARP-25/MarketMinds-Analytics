from django import forms
from .models import SubscriptionPlan
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class SubscriptionPlanForm(forms.ModelForm):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        custom_attribute_value = kwargs.pop('custom_attribute_value', None)
        super(SubscriptionPlanForm, self).__init__(*args, **kwargs)
        self.custom_attribute = custom_attribute_value
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Title... '
        self.fields['image'].widget.attrs['placeholder'] = 'Enter Image Path...'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description...'
        self.fields['price'].widget.attrs['placeholder'] = 'Enter Price...'
        self.fields['details'].widget.attrs['placeholder'] = 'Enter Details in this Format: Detail1, Detail2, Detail3...'
        self.fields['sku'].widget.attrs['placeholder'] = 'Enter SKU... Optional'
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        if self.custom_attribute == "edit":
            self.helper.add_input(Submit('submit', 'Edit Subscription Plan', css_class='button-62 btn-edit offset-2 col-8 addSubscriptionBtn custom-padding'))
        else:
            self.helper.add_input(Submit('submit', 'Add Subscription Plan', css_class='button-62 btn-edit offset-2 col-8 addSubscriptionBtn custom-padding'))
        self.helper.form_class = 'add-plan-form' 
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-plan-form-field' 
        self.helper.layout = Layout(
            'title',
            'image',
            'description',
            'price',
            'details',
            'sku',
        )
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
