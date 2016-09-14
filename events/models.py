from django.db import models
from codetributhon.behaviors import Timestampable


class Events(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'events'

    title = models.CharField(
        verbose_name='Titre',
        max_length=255,
        blank=False,
        null=False
    )

    subTitle = models.CharField(
        verbose_name='Sous-titre',
        max_length=255
    )

    enabled = models.BooleanField(
        verbose_name='Activer',
        null=False,
        blank=False,
        default=False
    )

    dateEvent = models.DateField(
        verbose_name='Date de l\'evenement',
        blank=False,
        null=False
    )

    time = models.TimeField(
        verbose_name='Heure',
        blank=False,
        null=False,
        default="00:00:00"
    )

    description = models.TextField(
        verbose_name='Description du projet'
    )

    location = models.CharField(
        verbose_name='Lieu',
        max_length=255,
        blank=False,
        null=False
    )

    presenter_picture = models.ImageField(
        upload_to="avatars_events",
        verbose_name='Presenter picture',
        blank=False,
    )

    url = models.URLField(
        verbose_name='URL',
        max_length=255,
        blank=False,
        null=False,
    )
    
    first_right_picture = models.ImageField(
        upload_to="avatars_events",
        verbose_name='First right picture',
        blank=True,
    )
    second_right_picture = models.ImageField(
        upload_to="avatars_events",
        verbose_name='Second right picture',
        blank=True,
    )
    thanking_text = models.TextField(
        verbose_name='Texte de remerciment des partenaires.'
    )

    def __str__(self):
        return self.title
