# Generated by Django 2.2.7 on 2019-11-15 16:31

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('orders', '0011_auto_20191115_1652'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OUTCity',
            new_name='Finish',
        ),
        migrations.RenameModel(
            old_name='InCity',
            new_name='Start',
        ),
    ]
