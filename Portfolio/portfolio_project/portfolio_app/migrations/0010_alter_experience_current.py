# Generated by Django 5.0 on 2024-04-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0009_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='current',
            field=models.CharField(choices=[('Working', 'Notice Period')], max_length=12),
        ),
    ]
