# Generated by Django 4.2.8 on 2024-03-07 21:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_subscriptionplan_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionplan',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]