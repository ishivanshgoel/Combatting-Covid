# Generated by Django 3.2 on 2021-04-27 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CoviHelp', '0004_remove_userinfo_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='state',
        ),
    ]