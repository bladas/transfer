from django.db import models
HOUR_Choices = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21'),
    ('22', '22'),
    ('23', '23'),

)
MINUTE_Choices = (
    ('0', '0'),
    ('5', '5'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20'),
    ('25', '25'),
    ('30', '30'),
    ('35', '35'),
    ('40', '40'),
    ('45', '45'),
    ('50', '50'),
    ('55', '55'),

)
Kids_Choices = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),

)


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
    lastname = models.CharField(max_length=50,null=True,blank=True)
    data = models.CharField(max_length=200)
    hours = models.CharField(choices=HOUR_Choices,blank=True, null=True,max_length=3)
    minutes = models.CharField(choices=MINUTE_Choices,blank=True, null=True,max_length=3)
    kolichestvo = models.ForeignKey(Kolichestvo,blank=True,on_delete=models.CASCADE, null=True)
    detey = models.CharField(choices=Kids_Choices,max_length=10,blank=True,null=True)
    deteydescr = models.CharField(max_length=10,blank=True,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    end = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    flag = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.name
