# Generated by Django 2.1.15 on 2024-02-04 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('imageUrl', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('isActive', models.BooleanField()),
            ],
        ),
    ]
