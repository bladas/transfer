from django.db import models

Start_Choices = (
    ('1', 'Из аеропорта Аликанте'),
    ('2', 'Из ареопорта Валенсии')
)

Type_car = (
    ('1', '1-4 пассажира,2-3 багажных места (легковой автомобиль)'),
    ('2', '5-6 пассажиров,4-5 багажных мест (минивэн)'),
    ('2', '7-8 пассажиров,6-8 багажных мест (микроавтобус)')
)

Space = (
    ('1', 'КАМПЕЛЬО /EL CAMPELLO'),
    ('2', 'ВИЛЬЯХОЙОСА / VILLAJOYOSA'),
    ('2', 'ФИНЕСТРАТ / FINESTRAT')
)


class Calculate(models.Model):
    start = models.CharField(max_length=20, choices=Start_Choices)
    type_car = models.CharField(max_length=50, choices=Type_car, default='1')
    kuda = models.CharField(max_length=50, choices=Space)
    price = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.start
