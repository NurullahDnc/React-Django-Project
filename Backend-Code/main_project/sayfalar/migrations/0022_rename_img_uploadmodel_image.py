# Generated by Django 4.2.9 on 2024-03-19 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0021_uploadmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadmodel',
            old_name='img',
            new_name='image',
        ),
    ]
