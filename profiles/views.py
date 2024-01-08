from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from bag.contexts import bag_contents
from subscription.models import SubscriptionPlan
from profiles.models import UserProfile
from checkout.models import ActiveSubscription

from .forms import UserProfileForm


def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    active_subscriptions = user_profile.get_active_subscriptions()
    return render(request, 'profiles/view_profile.html', {
        'user_profile': user_profile,
        'active_subscriptions': active_subscriptions,
    })


def edit_profile(request):
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
    subscription = get_object_or_404(ActiveSubscription, pk=subscription_id)
    if request.method == 'POST':
        subscription.delete()  
        messages.success(request, f"Subscription canceled successfully and will expire at: {subscription.end_date.strftime('%Y-%m-%d %H:%M')}.")

        return redirect('view_profile') 

    return redirect('view_profile') 