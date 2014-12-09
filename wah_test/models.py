from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheckIn(models.Model):
    when = models.DateTimeField('checked in', auto_now_add=True)
    name = models.CharField(max_length = 100, blank = True, default = '')
    room_id = models.SmallIntegerField(default = 0)

    class Meta:
        ordering = ('when',)

class Occupant(models.Model):
    # For auth, extend django user model.
    user = models.OneToOneField(User)

    # name = models.CharField(max_length = 100, blank = True, default = '')
    room_id = models.SmallIntegerField(default = 0)
    last_update = models.DateTimeField('date created', auto_now_add=True)

    def __unicode__(self):
        return self.user.username
        
