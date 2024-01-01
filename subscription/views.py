from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import SubscriptionPlan
from django.contrib import messages


class GetStarted(ListView):
    model = SubscriptionPlan
    template_name = 'get_started.html'
    context_object_name = 'subscription_plans'

    def post(self, request, *args, **kwargs):
        plan_id = request.POST.get('plan_id')
        bag_items = request.POST.getlist('bag_items')

        # Fetch the SubscriptionPlan based on the plan_id
        subscription_plan = get_object_or_404(SubscriptionPlan, id=plan_id)

        request.session['bag_items'].append(subscription_plan)
        print(f"bag_items:{bag_items}")


        # Include SubscriptionPlan details in the success message
        messages.success(request, f"Success!\n'{subscription_plan.title}' added to Shopping Bag")
        return redirect(request.path)
