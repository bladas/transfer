# Generated by Django 2.2.7 on 2019-11-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('otkuda', models.CharField(blank=True, max_length=150)),
                ('kuda', models.CharField(blank=True, max_length=150)),
                ('data', models.CharField(blank=True, max_length=150)),
                ('kolichestvo', models.CharField(blank=True, max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]
