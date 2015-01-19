from django.db import models


################################################################################
import jsonfield
class JSONFieldExample(models.Model):

    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now=True)
    recording_user = models.PositiveIntegerField(null=True, blank=True)

    flex_column    = jsonfield.JSONField()


################################################################################
from django_hstore import hstore
class HStoreExample(models.Model):

    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now=True)
    recording_user = models.PositiveIntegerField(null=True, blank=True)

    flex_column    = hstore.DictionaryField()

    objects = hstore.HStoreManager()


class HStoreSchemaExample(models.Model):

    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now=True)
    recording_user = models.PositiveIntegerField(null=True, blank=True)

    flex_column    = hstore.DictionaryField(schema=[
        {
            'name': 'my_number',
            'class': 'IntegerField',
            'kwargs': {
                'blank': True
            }
        },
        {
            'name': 'my_float',
            'class': 'FloatField',
            'kwargs': {
                'blank': True
            }
        }
    ])

    objects = hstore.HStoreManager()
