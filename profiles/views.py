from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from bag.contexts import bag_contents
from subscription.models import SubscriptionPlan
from profiles.models import UserProfile
from checkout.models import ActiveSubscription


from .forms import UserProfileForm


def view_profile(request):
    """
    View function to display user profile and active subscriptions.

    Retrieves the user's profile information and active subscriptions,
    then renders the 'view_profile.html' template with the user_profile
    and active_subscriptions data.

    Args:
    - request: HTTP request object.

    Returns:
    - Rendered 'view_profile.html' template displaying user profile and subscriptions.
    """
    user_profile = UserProfile.objects.get(user=request.user)
    active_subscriptions = user_profile.get_active_subscriptions()
    return render(request, 'profiles/view_profile.html', {
        'user_profile': user_profile,
        'active_subscriptions': active_subscriptions,
    })


def edit_profile(request):
    """
    View function to edit user profile information.

    Retrieves the user's profile information and handles form submission
    for updating the profile. If the form is valid, it saves the changes
    and redirects to the 'view_profile' page with a success message.

    Args:
    - request: HTTP request object.

    Returns:
    - Rendered 'edit_profile.html' template displaying the profile edit form.
      If the form is submitted and valid, redirects to 'view_profile' with a success message.
    """
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile Successfully updated!")
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=user_profile)
        
    return render(request, 'profiles/edit_profile.html', {'form': form})



def cancel_subscription(request, subscription_id):
    """
    View function to cancel an active subscription.

    Retrieves the subscription by ID and handles POST requests to cancel it.
    Upon cancellation, displays a success message and redirects to 'view_profile'.

    Args:
    - request: HTTP request object.
    - subscription_id: ID of the subscription to cancel.

    Returns:
    - If successful cancellation, redirects to 'view_profile' with a success message.
    - If not a POST request or subscription not found, redirects to 'view_profile'.
    """
    subscription = get_object_or_404(ActiveSubscription, pk=subscription_id)
    if request.method == 'POST':
        subscription.cancel_subscription()
        messages.success(request, f"Subscription canceled successfully and will expire at: {subscription.end_date.strftime('%Y-%m-%d %H:%M')}.")

        return redirect('view_profile') 

    return redirect('view_profile') 