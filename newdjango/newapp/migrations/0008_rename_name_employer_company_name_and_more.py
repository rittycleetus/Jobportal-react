# Generated by Django 5.0.6 on 2024-07-03 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_rename_name_jobseeker_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employer',
            old_name='name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='jobseeker',
            old_name='company_name',
            new_name='name',
        ),
    ]
