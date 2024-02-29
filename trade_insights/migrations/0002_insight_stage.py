# Generated by Django 4.2.8 on 2024-02-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_insights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insight',
            name='stage',
            field=models.CharField(choices=[('MS', 'Mainstage'), ('SS', 'Second Stage'), ('BS', 'Backstage')], default='BS', max_length=2),
        ),
    ]