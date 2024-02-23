from django.shortcuts import render
from subscription .models import SubscriptionPlan
from marketminds_analytics import settings

from django.core.mail import send_mail
from django.http import HttpResponse
from django.utils.dateformat import format


# Create your views here.
def index(request):
    """
    A View to return index page
    """
    return render(request, 'home/index.html')

def send_test_email(request):
    subscription_plan_titles = []
    subscription_plan_ids = request.session.get('bag_items', [])
    for id in subscription_plan_ids:
        subscription_plan = SubscriptionPlan.objects.get(id=id)
        subscription_plan_titles.append(subscription_plan.title)
    formatted_plan_titles = ", ".join(subscription_plan_titles)
    current_user = request.user
    active_subscriptions = current_user.active_subscriptions.all()
    if current_user.is_authenticated:
        user_profile = current_user.userprofile
        active_subscriptions_list = []
        for subscription in current_user.active_subscriptions.all():
            start_date = format(subscription.start_date, 'Y-m-d H:i')
            end_date = format(subscription.end_date, 'Y-m-d H:i')
            subscription_info = f"{subscription.subscription_plan.title} - Start: {start_date}, End: {end_date}"
            active_subscriptions_list.append(subscription_info)
        formatted_active_subscriptions = "\n".join(active_subscriptions_list)
    subject = 'Subscription Confirmation'
    message = (
        f"Dear {user_profile.full_name},\n\n"
        "We would like to extend our heartfelt thanks and appreciation for choosing to subscribe to our services. "
        f"We are delighted to welcome you as a new subscriber to our {formatted_plan_titles} plans.\n\n"
        "We are committed to providing our subscribers with the highest quality service and content. "
        "You can look forward to an enriching and informative experience with our subscriptions. "
        "Here are some important details about your subscription(s):\n\n"
        f"{formatted_active_subscriptions}\n"
        "\nShould you have any questions or require further information, please do not hesitate to contact us. "
        "You can reach us at support@marketminds.com or directly through your customer account on our website.\n\n"
        "We are excited to accompany and support you on your trading journey. "
        "Thank you for entrusting us with your business. We look forward to a long and successful partnership.\n\n"
        "Warm regards,\n\n"
        "Angelo Rocco Pucci\n"
        "Chief Executive Officer\n"
        "MarketMindsAnalytics"
    )
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['angelo.pucci@outlook.de'] 
    send_mail(subject, message, email_from, recipient_list)
    if 'bag_items' in request.session:
        del request.session['bag_items']

    return HttpResponse("Email sent successfully.")

