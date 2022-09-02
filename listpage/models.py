from django.db import models

class Bosses(models.Model):
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=255)
    boss_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name