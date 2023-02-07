from django.db import models
from stdimage import StdImageField

class Bosses(models.Model):
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=255)
    boss_image = StdImageField(upload_to='%y/%m/%d')
    loot = models.CharField(max_length=255)

    def __str__(self):
        return self.name