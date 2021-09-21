
import uuid

from django.db import models, transaction



# Create your models here.

"""
Ejemplo con relación.


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

class PersonsManager(models.Manager):

    def create_person(self, dni, name, lastname):
        with transaction.atomic():
            person = Person(name=name, lastname=lastname)
            person.save()
            ident = Identification(type=Identification.IdentificationTypes.DNI, number=dni, person=person)
            ident.save()
        return person

    """
    def create_person(self, dni, name, lastname):
        person = Person(name=name, lastname=lastname)
        person.save()
        i = Identification(type=Identification.IdentificationTypes.DNI, number=dni, person=person)
        i.save()
        return person
    """

class Person(models.Model):
    objects = PersonsManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024)
    lastname = models.CharField(max_length=1024)
    birthdate = models.DateField(null=True)

    def __str__(self):
        ids = [s.__str__() for s in self.identifications.all()]
        return f"{ids} {self.name} {self.lastname}"


class Identification(models.Model):

    class IdentificationTypes(models.TextChoices):
        DNI = 'DNI'
        PASSPORT = 'PASAPORTE'
        LC = 'LC'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(default=IdentificationTypes.DNI, choices=IdentificationTypes.choices, max_length=256)
    number = models.CharField(max_length=256)

    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='identifications')

    def __str__(self):
        return f"{self.type} {self.number}"        