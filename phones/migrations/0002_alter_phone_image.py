# Generated by Django 4.1.5 on 2023-01-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(),
        ),
    ]
