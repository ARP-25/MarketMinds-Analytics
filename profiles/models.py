from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from checkout.models import ActiveSubscription

class UserProfile(models.Model):
    """
    Model representing user profile information.

    Fields:
    - user: One-to-One relationship with the User model.
    - bio: Text field for user's bio or description.
    - birth_date: Date field for user's birth date.
    - full_name: Char field for user's full name.
    - email: Email field for user's email address.
    - phone_number: Char field for user's phone number.
    - country: Char field for user's country.
    - postcode: Char field for user's postal code.
    - town_or_city: Char field for user's town or city.
    - street_address1: Char field for user's street address (line 1).
    - street_address2: Char field for user's street address (line 2).
    - county: Char field for user's county.

    Methods:
    - get_active_subscriptions: Returns active subscriptions for the user.

    Signal Receiver:
    - create_or_update_user_profile: Creates or updates a user profile upon User creation or update.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    street_address1 = models.CharField(max_length=80, blank=True)
    street_address2 = models.CharField(max_length=80, blank=True)
    county = models.CharField(max_length=80, blank=True)

    def get_active_subscriptions(self):
        return ActiveSubscription.objects.filter(user=self.user)
    get_active_subscriptions.short_description = 'Active Subscriptions'
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
