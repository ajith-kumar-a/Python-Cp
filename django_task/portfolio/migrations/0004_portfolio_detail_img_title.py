# Generated by Django 4.2.15 on 2024-08-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_detail_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_detail',
            name='img_title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
