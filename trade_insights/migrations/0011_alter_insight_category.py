# Generated by Django 4.2.8 on 2024-03-17 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0008_alter_subscriptionplan_image'),
        ('trade_insights', '0010_alter_insight_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='category',
            field=models.ForeignKey(default=39, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='insights', to='subscription.subscriptionplan'),
        ),
    ]