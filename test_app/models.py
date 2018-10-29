from django.db import models

# Create your models here.
from akoikelov.djazz.models import AbstractModel


class Student(AbstractModel):
    class Meta:
        verbose_name_plural = ''
        verbose_name = ''

    first_name = models.CharField(verbose_name='first_name', max_length=255, unique=False, null=False)
    last_name = models.CharField(verbose_name='last_name', max_length=255, unique=False, null=False)
    age = models.IntegerField(verbose_name='age', null=False)

    _gen_data = True

    def __unicode__(self):
        return ''