# Generated by Django 5.0 on 2024-04-25 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_rename_file_resume_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='resume',
            new_name='resumes',
        ),
    ]