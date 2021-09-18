import uuid

from django.db import models
from django.db.models.enums import Choices


from persons.models import Person

# Create your models here.


class SocialSecurityInvoice(models.Model):

    number = models.IntegerField()
    paid = models.BooleanField()


class Extraction(models.Model):

    date = models.DateField()
    cost = models.IntegerField()
    paid = models.BooleanField()


class LabResult(models.Model):

    class LabResultSentType(models.TextChoices):
        SENT = 'Enviado'
        PENDING = 'Pendiente'
        DOEST_APPLY = 'No Aplica'    


    class LabResultDescription(models.TextChoices):
        NEGATIVE = 'Negativo'
        POSITIVE = 'Positivo'

    result = models.TextField(choices=LabResultDescription.choices, null=True)
    sent = models.TextField(choices=LabResultSentType.choices, max_length=256, default=LabResultSentType.PENDING)


class LabQuote(models.Model):
    cost = models.IntegerField()
    date = models.DateField()
    

class LabType(models.Model):

    name = models.CharField(max_length=1024)


class Lab(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    patient = models.ForeignKey(Person, related_name='labs', on_delete=models.CASCADE)
    medic = models.ForeignKey(Person, related_name='derived_labs', on_delete=models.CASCADE)
    diagnosis = models.TextField(max_length=1024)
    type = models.ForeignKey(LabType, on_delete=models.CASCADE)
    result = models.ForeignKey(LabResult, on_delete=models.CASCADE)

    quote = models.ForeignKey(LabQuote, null=True, on_delete=models.SET_NULL)


class LabStatus(models.Model):

    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.TextField()


