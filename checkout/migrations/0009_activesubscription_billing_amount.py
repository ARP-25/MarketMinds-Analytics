# Generated by Django 4.2.8 on 2024-03-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_activesubscription_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activesubscription',
            name='billing_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]