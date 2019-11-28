from django.db import models


class Excursion(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    img = models.ImageField('img', null=True, blank=True, upload_to='excursions')

    def __str__(self):
        return self.name