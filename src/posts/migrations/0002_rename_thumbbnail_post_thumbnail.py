# Generated by Django 5.0.1 on 2024-02-06 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumbbnail',
            new_name='thumbnail',
        ),
    ]