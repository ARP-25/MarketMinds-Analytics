# Generated by Django 4.2.8 on 2024-01-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='profile',
            name='county',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='postcode',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='street_address1',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='profile',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='profile',
            name='town_or_city',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
