# Generated by Django 3.1 on 2020-08-16 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscriber',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]