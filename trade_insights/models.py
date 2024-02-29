from django.db import models
from ckeditor.fields import RichTextField
from profiles.models import UserProfile  
from subscription.models import SubscriptionPlan


class Insight(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    content = RichTextField()
    category = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE, related_name='insights')
    short_description = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='authored_insights')

    MAINSTAGE = 'MS'
    SECOND_STAGE = 'SS'
    BACKSTAGE = 'BS'
    STAGE_CHOICES = [
        (MAINSTAGE, 'Mainstage'),
        (SECOND_STAGE, 'Second Stage'),
        (BACKSTAGE, 'Backstage'),
    ]
    stage = models.CharField(
        max_length=2,
        choices=STAGE_CHOICES,
        default=BACKSTAGE,
    )

    def __str__(self):
        return self.title
