from django import forms
from trade_insights.models import Insight
from django_summernote.widgets import SummernoteWidget

class InsightForm(forms.ModelForm):
    """
    A Django ModelForm for the Insight model.

    This form is used for creating and editing Insight objects. It provides fields for 
    entering details like title, release date, content, category, etc. The form also includes
    specific widgets to enhance the user interface, such as a date picker for the release date
    and a rich text editor (Summernote) for the content.

    Attributes:
    - Meta.model: Specifies the Insight model that this form is linked to.
    - Meta.fields: Defines the fields that are included in the form. This includes 'title', 
      'release_date', 'content', 'category', 'short_description', 'author', 'cover_image', 
      'stage', and 'display'.
    - Meta.widgets: Provides custom widgets for certain fields. For 'release_date', it uses 
      a date input, and for 'content', it uses the SummernoteWidget to allow rich text editing.

    Notes:
    - This form can be used in views that handle the creation and modification of Insight objects.
    """
    class Meta:
        model = Insight
        fields = ['title', 'release_date', 'content', 'category', 'short_description', 'author', 'cover_image', 'stage', 'display']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'content': SummernoteWidget(),
        }