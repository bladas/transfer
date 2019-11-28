from django.db import models


class Start(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Finish(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Kolichestvo(models.Model):

    kolichestvo = models.CharField(max_length=10)

    def __str__(self):
        return self.kolichestvo


class Order(models.Model):
    name = models.CharField(max_length=50)

    otkuda = models.ForeignKey(Start,blank=True,on_delete=models.CASCADE,null=True)
    kuda = models.ForeignKey(Finish,blank=True ,on_delete=models.CASCADE,null=True)
    lastname = models.CharField(max_length=50)
    data = models.DateField()
    hours = models.TimeField(blank=True, null=True)
    kolichestvo = models.ForeignKey(Kolichestvo,blank=True,on_delete=models.CASCADE, null=True)
    detey = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    end = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    flag = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name
