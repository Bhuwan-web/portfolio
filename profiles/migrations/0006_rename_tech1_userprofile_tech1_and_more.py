# Generated by Django 4.0 on 2022-01-21 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_userprofile_tech1_userprofile_tech2_userprofile_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Tech1',
            new_name='tech1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='Tech2',
            new_name='tech2',
        ),
    ]