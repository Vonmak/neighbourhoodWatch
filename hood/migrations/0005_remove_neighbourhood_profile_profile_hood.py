# Generated by Django 4.0.5 on 2022-06-17 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_remove_neighbourhood_user_neighbourhood_admin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='hood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='members', to='hood.neighbourhood'),
        ),
    ]
