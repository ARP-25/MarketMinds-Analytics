# Generated by Django 4.2.8 on 2024-03-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_insights', '0013_alter_insight_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='content',
            field=models.TextField(),
        ),
    ]