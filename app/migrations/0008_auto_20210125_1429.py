# Generated by Django 3.0.5 on 2021-01-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210125_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='calories',
            field=models.IntegerField(default=0),
        ),
    ]
