# Generated by Django 5.0.6 on 2024-07-03 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0008_rename_name_employer_company_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employer',
        ),
        migrations.DeleteModel(
            name='TempEmployerProfile',
        ),
    ]
