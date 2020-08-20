from django.db import models

from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django_countries.fields import CountryField


class Cheese(TimeStampedModel):
    name = models.CharField('Name of Cheese', max_length=255)
    slug = AutoSlugField('Cheese Address',
        unique=True, always_update=False, populate_from='name')
    description = models.TextField('Description', blank=True)
    country_of_origin = CountryField("Pays d'origine", blank=True)

    class Firmess(models.TextChoices):
        UNSPECIFIED = 'unspecified', 'Unspecified'
        SOFT = 'soft', 'Soft'
        SEMI_SOFT = 'semi-soft', 'Semi-soft'
        SEMI_HARD = 'semi-hard', 'Semi-hard'
        HARD = 'hard', 'Hard'
    
    firmess = models.CharField('Firmess', max_length=20,
        choices=Firmess.choices, default=Firmess.UNSPECIFIED)

    def __str__(self):
        return self.name