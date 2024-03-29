# Generated by Django 4.2.8 on 2024-03-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_activesubscription_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activesubscription',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='activesubscription',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='activesubscription',
            name='start_date',
        ),
        migrations.AddField(
            model_name='activesubscription',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='activesubscription',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
    ]
