# Generated by Django 2.2.5 on 2020-09-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_remove_group_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_user',
            field=models.ManyToManyField(blank=True, related_name='user_user', to='login.User'),
        ),
    ]