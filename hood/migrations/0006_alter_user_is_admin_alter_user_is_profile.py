# Generated by Django 4.0.5 on 2022-06-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_remove_neighbourhood_profile_profile_hood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_profile',
            field=models.BooleanField(default=False, verbose_name='Member'),
        ),
    ]