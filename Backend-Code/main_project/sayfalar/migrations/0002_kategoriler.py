# Generated by Django 2.1.15 on 2024-02-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='kategoriler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
    ]