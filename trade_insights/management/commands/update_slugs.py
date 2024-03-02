from django.core.management.base import BaseCommand
from django.utils.text import slugify
from trade_insights.models import Insight

class Command(BaseCommand):
    help = 'Updates slugs for all Insights'

    def handle(self, *args, **kwargs):
        insights = Insight.objects.all()
        for insight in insights:
            insight.slug = slugify(insight.title)
            insight.save()
            self.stdout.write(self.style.SUCCESS(f'Updated slug for "{insight.title}"'))
