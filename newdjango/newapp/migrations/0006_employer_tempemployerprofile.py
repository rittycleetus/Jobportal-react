# Generated by Django 5.0.6 on 2024-07-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_jobseeker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TempEmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('dob', models.DateField(verbose_name='date of birth')),
                ('username', models.CharField(blank=True, max_length=50, null=True, verbose_name='username')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='temp_employer_profile_pictures/', verbose_name='profile picture')),
                ('educational_info', models.TextField(blank=True, null=True, verbose_name='educational information')),
                ('address', models.TextField(blank=True, null=True, verbose_name='address')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]