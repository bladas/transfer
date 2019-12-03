from django.db import models


#
# Start_Choices = (
#     ('1', 'Из аеропорта Аликанте'),
#     ('2', 'Из ареопорта Валенсии')
# )
#
# Type_car = (
#     ('1', '1-4 пассажира,2-3 багажных места (легковой автомобиль)'),
#     ('2', '5-6 пассажиров,4-5 багажных мест (минивэн)'),
#     ('3', '7-8 пассажиров,6-8 багажных мест (микроавтобус)')
# )
#
# Space = (
#     ('1', 'КАМПЕЛЬО /EL CAMPELLO'),
#     ('2', 'ВИЛЬЯХОЙОСА / VILLAJOYOSA'),
#     ('3', 'ФИНЕСТРАТ / FINESTRAT'),
#     ('4', 'БЕНИДОРМ / BENIDORM'),
#     ('5', 'АЛЬБИР / ALBIR'),
#     ('6', 'АЛТЕА / ALTEA'),
#     ('7', 'КАЛЬПЕ / CALPE'),
#     ('8', 'БЕНИССА / BENISSA'),
#     ('9', 'ТЕУЛАДА / TEULADA'),
#     ('10', 'МОРАЙРА / MORAIRA'),
#     ('11', 'ХАВЕА / JAVEA'),
#     ('12', 'ДЕНИЯ / DENIA'),
#     ('13', 'ОНДАРА / ONDARA'),
#     ('14', 'ОЛИВА / OLIVA'),
#     ('15', 'ГАНДИЯ / GANDIA')
# )
#

class Start(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Space(models.Model):
    start = models.ForeignKey(Start, on_delete=models.CASCADE)

    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class TypeCar(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


class Calculate(models.Model):
    start = models.ForeignKey(Start, on_delete=models.CASCADE)
    type_car = models.ForeignKey(TypeCar, on_delete=models.CASCADE)
    kuda = models.ForeignKey(Space, on_delete=models.CASCADE)
    price = models.CharField(max_length=50, blank=True, null=True)

    def serialize(self):
        return self.__dict__

    def __str__(self):
        return str(self.pk) + ' ' + self.price


class OrderCalculates(models.Model):
    start = models.ForeignKey(Start, on_delete=models.CASCADE)
    type_car = models.ForeignKey(TypeCar, on_delete=models.CASCADE)
    kuda = models.ForeignKey(Space, on_delete=models.CASCADE)
    price = models.CharField(max_length=50, blank=True, null=True)

    def serialize(self):
        return self.__dict__

    def __str__(self):
        return str(self.pk) + ' ' + self.price
