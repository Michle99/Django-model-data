# Generated by Django 4.1.7 on 2023-03-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0002_remove_dog_adoption_date_alter_dog_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
