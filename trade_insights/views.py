from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Insight

# Create your views here.
def trade_insights(request):
    # Filtern der Insights für Main Stage und Second Stage
    ms_insights = Insight.objects.filter(stage='MS')
    ss_insights = Insight.objects.filter(stage='SS')

    # Beide Listen in den Kontext einfügen
    context = {
        'ms_insights': ms_insights,
        'ss_insights': ss_insights,
    }

    # Kontext an das Template übergeben
    return render(request, 'trade_insights/trade_insights.html', context)