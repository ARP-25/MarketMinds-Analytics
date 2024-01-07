from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from .models import SubscriptionPlan
from django.contrib import messages
from .forms import SubscriptionPlanForm

class GetStarted(ListView):
    model = SubscriptionPlan
    template_name = 'get_started.html'
    context_object_name = 'subscription_plans'


class AdminAccess(ListView):
    model = SubscriptionPlan
    template_name = 'admin_access.html'
    context_object_name = 'subscription_plans'

    def post(self, request, *args, **kwargs):
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'sort_plan':
                # Logik für "Sort Plans" POST-Request
                return HttpResponse("Sort Plans ausgeführt!")
            elif action == 'delete_plan':
                # Logik für "Delete Plan" POST-Request
                return HttpResponse("Delete Plan ausgeführt!")


def admin_access_add(request):
    if request.method == 'POST':
        form = SubscriptionPlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Successfully added new Subscription Plan!')
            return redirect('admin_access')  
    else:
        form = SubscriptionPlanForm()   
    return render(request, 'admin_access_add.html', {'form': form})


def admin_access_delete(request, subscription_id):
    subscriptionPlan = get_object_or_404(SubscriptionPlan, pk=subscription_id)
    if request.method == 'POST':
        subscriptionPlan.delete()  
        messages.success(request, 'Subscription Plan deleted successfully.')
        return redirect('admin_access')  
    return redirect('admin_access')  


