# Generated by Django 4.2.8 on 2024-03-15 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscription', '0008_alter_subscriptionplan_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField()),
                ('total_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('monthly_recurring_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('new_subscriptions', models.IntegerField(default=0)),
                ('canceled_subscriptions', models.IntegerField(default=0)),
                ('new_subscription_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('canceled_subscription_revenue', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlanMetrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active_subscriptions_count', models.IntegerField(default=0)),
                ('financial_metrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_metrics.financialmetrics')),
                ('subscription_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.subscriptionplan')),
            ],
        ),
        migrations.AddField(
            model_name='financialmetrics',
            name='plan_metrics',
            field=models.ManyToManyField(through='platform_metrics.PlanMetrics', to='subscription.subscriptionplan'),
        ),
    ]
