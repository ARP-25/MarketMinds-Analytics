# Generated by Django 4.2.8 on 2024-03-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0007_rename_stripe_plan_id_subscriptionplan_stripe_price_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionplan',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
