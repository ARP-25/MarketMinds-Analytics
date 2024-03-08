from django import forms
from trade_insights.models import Insight
from django_summernote.widgets import SummernoteWidget

class InsightForm(forms.ModelForm):
    class Meta:
        model = Insight
        fields = ['title', 'release_date', 'content', 'category', 'short_description', 'author', 'cover_image', 'stage', 'display']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'content': SummernoteWidget(),
        }