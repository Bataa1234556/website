# Generated by Django 5.0.6 on 2024-06-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
