# Generated by Django 2.2.7 on 2019-11-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0021_order_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='flag',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
