# Generated by Django 2.2.7 on 2019-11-15 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20191115_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='lastname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
