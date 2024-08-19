# Generated by Django 4.2.15 on 2024-08-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_detail',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='portfolio_detail',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='portfolio_detail',
            name='full_name',
            field=models.SlugField(default='', editable=False),
        ),
        migrations.AddField(
            model_name='portfolio_detail',
            name='read_more',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
