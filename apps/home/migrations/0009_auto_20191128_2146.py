# Generated by Django 2.2.7 on 2019-11-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_calculator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculate',
            name='start',
            field=models.CharField(choices=[('Из аеропорта Аликанте', 'Из аеропорта Аликанте'), ('Из ареопорта Валенсии', 'Из ареопорта Валенсии')], max_length=20),
        ),
    ]
