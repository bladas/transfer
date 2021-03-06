# Generated by Django 2.2.7 on 2019-11-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191128_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculate',
            name='kuda',
            field=models.CharField(choices=[('1', 'КАМПЕЛЬО /EL CAMPELLO'), ('2', 'ВИЛЬЯХОЙОСА / VILLAJOYOSA'), ('3', 'ФИНЕСТРАТ / FINESTRAT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='calculate',
            name='start',
            field=models.CharField(choices=[('1', 'Из аеропорта Аликанте'), ('2', 'Из ареопорта Валенсии')], max_length=20),
        ),
        migrations.AlterField(
            model_name='calculate',
            name='type_car',
            field=models.CharField(choices=[('1', '1-4 пассажира,2-3 багажных места (легковой автомобиль)'), ('2', '5-6 пассажиров,4-5 багажных мест (минивэн)'), ('3', '7-8 пассажиров,6-8 багажных мест (микроавтобус)')], default='1', max_length=50),
        ),
    ]
