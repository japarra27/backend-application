from django.db import models
from rest_framework import serializers
from django.conf import settings

# Create your models here.


class CrearEvento(models.Model):
    id = serializers.ReadOnlyField()
    event_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_name = models.CharField('Nombre del evento', max_length=128)
    category = (("1", 'Conferencia'), ("2", 'Seminario'),
                ("3", 'Congreso'), ("4", 'Curso'))
    event_category = models.CharField("Categoría del evento",
                                      max_length=16, choices=category, null=False, blank=False)
    event_place = models.CharField('Lugar del evento', max_length=128)
    event_address = models.CharField('Dirección del evento', max_length=128)
    event_initial_date = models.DateTimeField("Fecha inicial del evento")
    event_final_date = models.DateTimeField("Fecha final del evento")
    category_event = (("1", 'Virtual'), ("2", 'Presencial'))
    event_type = models.CharField("Modalidad del evento",
                                  max_length=10, choices=category_event, null=False, blank=False)
    thumbnail = models.ImageField("Imagen",
                                  upload_to="recipe_thumbnails", default="recipe_thumbnails/default.png")

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ('-id',)