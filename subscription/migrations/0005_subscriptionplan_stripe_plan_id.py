# Generated by Django 4.2.8 on 2024-03-11 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0004_subscriptionplan_staged'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='stripe_plan_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
