# Generated by Django 4.2.8 on 2024-03-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_insights', '0005_insight_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='stage',
            field=models.CharField(choices=[('MS', 'Mainstage'), ('SS', 'Secondstage'), ('BS', 'Backstage')], default='BS', max_length=2),
        ),
    ]
