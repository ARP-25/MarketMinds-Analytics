from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from checkout.models import ActiveSubscription

class UserProfile(models.Model):
    """
    A Django model representing additional information for a user.

    This model extends the base User model by adding more fields specific to the user's profile. It includes personal details and contact information along with Stripe-related data for handling subscriptions.

    Attributes:
        user (OneToOneField): A one-to-one relationship with Django's built-in User model.
        email (EmailField): The email address of the user. It's synchronized with the email in the User model.
        stripe_customer_id (CharField): The Stripe customer ID for the user, used in subscription billing processes.

    Methods:
        get_active_subscriptions(self): Returns the queryset of active subscriptions associated with the user.

    The __str__ method provides a readable string representation of the UserProfile, useful in Django's admin interface or in debugging output.

    Signal Receiver:
        A receiver function that creates or updates the UserProfile instance whenever a User instance is saved.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    stripe_customer_id = models.CharField(max_length=255, null=True, blank=True)
    
    def get_active_subscriptions(self):
        """
        Retrieves active subscriptions associated with the user.

        Returns:
            QuerySet: A queryset of ActiveSubscription objects linked to the user.
        """
        return ActiveSubscription.objects.filter(user=self.user)
    
    get_active_subscriptions.short_description = 'Active Subscriptions'
    
    def __str__(self):
        """
        Provides a human-readable representation of the UserProfile.

        Returns:
            str: A string representation including the username, email, and Stripe customer ID.
        """
        return f"{self.user}"

        
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates or updates a UserProfile instance upon User instance creation or update.

    When a new User instance is created, this function creates a corresponding UserProfile instance with the user's email. If the User instance is being updated, it updates the associated UserProfile's email.

    Args:
        sender (Model): The model class that sent the signal. In this case, it's User.
        instance (User): The actual instance of the User being saved.
        created (bool): A boolean indicating if a new record was created.
        **kwargs: Additional keyword arguments.

    Returns:
        None: This function does not return anything but saves or updates UserProfile instances.
    """
    if created:
        UserProfile.objects.create(user=instance, email=instance.email)
    else:
        # Update the user profile only if it already exists
        user_profile, profile_created = UserProfile.objects.get_or_create(user=instance)
        if not profile_created:  # If the profile was not just created, update the email
            user_profile.email = instance.email
            user_profile.save()
