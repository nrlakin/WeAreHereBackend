from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheckIn(models.Model):
    when = models.DateTimeField(auto_now_add=True, editable = False)
    room_id = models.SmallIntegerField(default = 0)
    user = models.ForeignKey('auth.User', related_name = 'checkins')

    def save(self, *args, **kwargs):
        super(CheckIn, self).save(*args, **kwargs)

    class Meta:
        ordering = ('when',)
        get_latest_by = 'when'

    def __unicode__(self):
        return str(self.when) + ': ' + str(self.room_id)

class Occupant(models.Model):
    # For auth, extend django user model.
    user = models.OneToOneField(User)

    # name = models.CharField(max_length = 100, blank = True, default = '')
    room_id = models.SmallIntegerField(default = 0)
    last_update = models.DateTimeField('date created', auto_now_add=True)

    def __unicode__(self):
        return self.user.username
