# Generated by Django 2.2.7 on 2019-11-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_auto_20191120_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='end',
            field=models.BooleanField(default=False),
        ),
    ]
