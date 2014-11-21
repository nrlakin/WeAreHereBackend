from django.db import models

# Create your models here.
class CheckIn(models.Model):
    when = models.DateTimeField('checked in', auto_now_add=True)
    name = models.CharField(max_length = 100, blank = True, default = '')
    room = models.CharField(max_length = 100, blank = True, default = '')

    class Meta:
        ordering = ('when',)

class Occupant(models.Model):
    name = models.CharField(max_length = 100, blank = True, default = '')
    room = models.CharField(max_length = 100, blank = True, default = '')
    last_update = models.DateTimeField('date created', auto_now_add=True)

    class Meta:
        ordering = ('name',)
