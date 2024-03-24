from django.core.mail import send_mail
from django.conf import settings
from django.utils.dateformat import format
from subscription.models import SubscriptionPlan 
from checkout.models import ActiveSubscription

def send_subscription_confirmation_email(user):
    """
    Send a subscription confirmation email to the user after successful checkout.

    This function fetches details of active subscriptions for the authenticated user
    and formats them for inclusion in the email body. It also clears 'bag_items'
    from the session after sending the email.

    Args:
    - request (HttpRequest): The HTTP request object from the checkout success view.
    """
    current_user = user
    if current_user.is_authenticated and current_user.email:
        active_subscriptions = ActiveSubscription.objects.filter(user=current_user)
        active_subscriptions_list = []

        for subscription in active_subscriptions:
            start_date = format(subscription.start_date, 'Y-m-d H:i') if subscription.start_date else 'Date not set'
            renewal_date = format(subscription.renewal_date, 'Y-m-d H:i') if subscription.renewal_date else 'Date not set'
            subscription_info = (
                f"Plan: {subscription.subscription_plan.title}\n"
                f"Start Date: {start_date}\n"
                f"Next Renewal Date: {renewal_date}\n\n"
            )
            active_subscriptions_list.append(subscription_info)

        formatted_active_subscriptions = "".join(active_subscriptions_list)

        email_body = (
            f"Dear {current_user.username},\n\n"
            "Thank you for subscribing to our services at MarketMindsAnalytics. "
            "We are excited to have you on board and look forward to contributing to your success.\n\n"
            "Below are the details of your active subscription(s):\n\n"
            f"{formatted_active_subscriptions}"
            "We are here to support you every step of the way. Should you have any questions or need assistance, "
            "feel free to contact us at any time.\n\n"
            "Best regards,\n"
            "The MarketMindsAnalytics Team"
        )

        send_mail(
            subject="Confirmation Email - Subscription",
            message=email_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[current_user.email],
        )

    else:
        print(f"Email not sent. User {current_user.username} has no email address.")

