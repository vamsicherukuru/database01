# Generated by Django 3.0.3 on 2020-07-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChristKart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
    ]
