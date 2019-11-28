from django.db import models


class TransferAlikante(models.Model):
    name = models.CharField(max_length=20)
    ispanename = models.CharField(max_length=20)
    pricelehkovoy = models.CharField(max_length=5)
    priceminiven = models.CharField(max_length=5)
    pricemikroavto = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class TransferValencia(models.Model):
    name = models.CharField(max_length=20)
    ispanename = models.CharField(max_length=20)
    pricelehkovoy = models.CharField(max_length=5)
    priceminiven = models.CharField(max_length=5)
    pricemikroavto = models.CharField(max_length=5)

    def __str__(self):
        return self.name
