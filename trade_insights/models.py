from django.db import models
from django.utils.text import slugify
from profiles.models import UserProfile  
from subscription.models import SubscriptionPlan


# Used as Backup in Case SubscriptionPlan with associated Insight got deleted
# So template wont try to render a Null Field when SubscriptionPlan is deleted
DEFAULT_SUBSCRIPTION_PLAN_ID = 39



class Insight(models.Model):
    title = models.CharField(max_length=200, unique=True)

    slug = models.SlugField(max_length=200, blank=True, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Insight, self).save(*args, **kwargs)

    release_date = models.DateField()
    content = models.TextField()
    category = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_DEFAULT, default=DEFAULT_SUBSCRIPTION_PLAN_ID, related_name='insights')
    short_description = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='authored_insights')

    cover_image = models.ImageField(      
    upload_to='images/', 
    null=True, 
    blank=True
    )

    MAINSTAGE = 'MS'
    SECOND_STAGE = 'SS'
    BACKSTAGE = 'BS'
    STAGE_CHOICES = [
        (MAINSTAGE, 'Mainstage'),
        (SECOND_STAGE, 'Secondstage'),
        (BACKSTAGE, 'Backstage'),
    ]
    stage = models.CharField(
        max_length=2,
        choices=STAGE_CHOICES,
        default=BACKSTAGE,
    )

    TEXT = 'TXT'
    IMAGE = 'IMG'
    DISPLAY_CHOICES = [
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
    ]
    display = models.CharField(
        max_length=3,
        choices=DISPLAY_CHOICES,
        default=IMAGE,
    )

    def __str__(self):
        return self.title
