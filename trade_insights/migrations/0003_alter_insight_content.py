# Generated by Django 4.2.8 on 2024-02-29 16:26
from django.db import models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_insights', '0002_insight_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='content',
            field=models.TextField()
        ),
    ]
