# Generated by Django 4.2.9 on 2024-02-11 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayfalar', '0006_remove_cars_categori'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='kategoriler',
            new_name='categories',
        ),
        migrations.AddField(
            model_name='cars',
            name='home_categori',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sayfalar.categories'),
        ),
    ]
