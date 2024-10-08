# Generated by Django 4.2.15 on 2024-08-19 06:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(18)])),
                ('job_details', models.CharField(max_length=30)),
                ('caption', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
