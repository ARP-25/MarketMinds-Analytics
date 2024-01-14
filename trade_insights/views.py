from django.shortcuts import render

# Create your views here.
def trade_insights(request):

    return render(request, 'trade_insights/trade_insights.html')