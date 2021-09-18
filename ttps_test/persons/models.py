from django.db import models

# Create your models here.

"""
class IdentificationType(models.Model):
    id_type = models.CharField(max_length=256)

    def __str__(self):
        return self.id_type

class Identification(models.Model):
    id_type = models.ForeignKey(IdentificationType, on_delete=models.CASCADE)
    number = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.id_type.id_type} {self.number}"

"""

class Identification(models.Model):

    class IdentificationTypes(models.TextChoices):
        DNI = 'DNI'
        PASSPORT = 'PASAPORTE'
        LC = 'LC'

    type = models.CharField(default=IdentificationTypes.DNI, choices=IdentificationTypes.choices, max_length=256)
    number = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.type} {self.number}"

class Person(models.Model):
    name = models.CharField(max_length=1024)
    lastname = models.CharField(max_length=1024)

    def __str__(self):
        return f"{self.name} {self.lastname}"