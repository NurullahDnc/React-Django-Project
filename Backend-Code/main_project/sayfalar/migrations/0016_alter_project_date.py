# Generated by Django 4.2.9 on 2024-02-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0015_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
