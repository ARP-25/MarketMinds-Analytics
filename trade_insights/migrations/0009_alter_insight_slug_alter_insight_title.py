# Generated by Django 4.2.8 on 2024-03-02 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_insights', '0008_alter_insight_slug_alter_insight_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
