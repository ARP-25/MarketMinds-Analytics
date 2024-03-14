from django.db import models

# Create your models here.
class SubscriptionPlan(models.Model):
    """
    Model representing a subscription plan.

    Fields:
    - title: CharField for the title of the subscription plan.
    - image: ImageField for uploading an image related to the plan.
    - description: TextField for describing the subscription plan.
    - price: DecimalField for the price of the subscription plan.
    - details: TextField for additional details about the plan.
    - sku: CharField for the stock keeping unit (optional).

    Methods:
    - __str__: String representation of the subscription plan, returns its title.
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True) 
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    staged = models.BooleanField(default=False)
    stripe_price_id = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title

