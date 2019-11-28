from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    img = models.ImageField('img', null=True, blank=True, upload_to='services')

    def __str__(self):
        return self.name