# Generated by Django 5.1.7 on 2025-03-29 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addmoney',
            name='valuta',
            field=models.CharField(default='USD', max_length=10),
        ),
    ]
