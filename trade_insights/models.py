from django.db import models
from django.utils.text import slugify
from profiles.models import UserProfile  
from subscription.models import SubscriptionPlan


# Used as Backup in Case SubscriptionPlan with associated Insight got deleted
# So template wont try to render when a Null Field when SubscriptionPlan is deleted
DEFAULT_SUBSCRIPTION_PLAN_ID = 39


class Insight(models.Model):
    """
    A model representing an 'Insight' which could be an article, analysis, or report associated 
    with a subscription plan.

    This model captures details like the title, content, author, and category of the insight. 
    The 'category' is a ForeignKey to SubscriptionPlan, making each insight associated with a 
    specific subscription plan. The model uses a slug field for SEO-friendly URLs. The 'stage' 
    and 'display' fields allow for flexible presentation options in templates.

    Attributes:
        - title (CharField): The title of the insight.
        - slug (SlugField): An automatically generated slug for the insight. This is based on 
          the title and is used in URLs.
        - release_date (DateField): The date when the insight is published or released.
        - content (TextField): The main body of the insight.
        - category (ForeignKey to SubscriptionPlan): The subscription plan associated with the 
          insight. Uses a default value as a fallback in case the linked SubscriptionPlan is deleted.
        - short_description (TextField): A brief summary or description of the insight.
        - author (ForeignKey to UserProfile): The author of the insight. This can be null if not specified.
        - cover_image (ImageField): An optional image associated with the insight.
        - stage (CharField): A field to categorize the insight into various stages like 'Mainstage', 
          'Secondstage', or 'Backstage'.
        - display (CharField): Specifies how the insight should be displayed, either as text or image.

    Methods:
        - save: Overridden to automatically generate a slug based on the title.
        - __str__: Returns the title of the insight.

    Notes:
        - The Insight model is designed to support content management for subscription-based 
          services where insights are tied to specific subscription plans.
        - The use of 'DEFAULT_SUBSCRIPTION_PLAN_ID' ensures the integrity of the model if related 
          SubscriptionPlans are deleted.
        - The 'slug' field enhances SEO and user-friendliness of URLs in a web application context.
    """
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
