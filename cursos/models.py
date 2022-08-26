from django.db import models


class Courses(models.Model):
  name = models.CharField(max_length=50)
  activated = models.BooleanField()
  price = models.CharField(max_length=3)
  def __str__(self):
    return self.name