# Generated by Django 4.2.8 on 2024-03-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_activesubscription_monthly_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='activesubscription',
            name='current_period_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
