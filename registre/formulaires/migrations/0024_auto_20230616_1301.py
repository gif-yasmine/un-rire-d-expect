# Generated by Django 3.1.14 on 2023-06-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0023_auto_20230616_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spirit',
            name='date',
            field=models.DateField(blank=True, default=None),
        ),
    ]
