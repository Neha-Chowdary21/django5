# Generated by Django 4.2.6 on 2024-04-26 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_remove_userprofile_aadhar_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]