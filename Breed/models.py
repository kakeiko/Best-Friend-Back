from django.db import models
import uuid


class DogBreed(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    name = models.CharField(null=False, blank=False, max_length=100, unique=True)
    origin = models.CharField(null=True, blank=True, max_length=100)
    group = models.CharField(null=False, blank=True, max_length=100)
    life_span = models.CharField(null=True, blank=True, max_length=100)
    temperament = models.CharField(null=False, blank=True, max_length=1000)
    weight = models.CharField(null=True, blank=True, max_length=100)
    height = models.CharField(null=True, blank=True, max_length=100)
    description = models.CharField(null=False, blank=True, max_length=1000)
