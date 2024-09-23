from django.db import models

# Create your models here.
class CityList(models.Model):
    """
    城市表
    """
    city = models.CharField(max_length=100)

