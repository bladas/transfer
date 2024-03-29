# Generated by Django 2.2.7 on 2019-12-02 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20191202_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
                ('kuda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Space')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Start')),
                ('type_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.TypeCar')),
            ],
        ),
        migrations.CreateModel(
            name='OrderCalculates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
                ('kuda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Space')),
                ('start', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Start')),
                ('type_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.TypeCar')),
            ],
        ),
        migrations.DeleteModel(
            name='Calculates',
        ),
    ]
