# Generated by Django 4.2.8 on 2024-03-12 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_activesubscription_billing_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='activesubscription',
            name='monthly_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
