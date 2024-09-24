from django.db import models

# Create your models here.
class ProvinceList(models.Model):
    """
    城市表
    """
    Provinces = models.CharField(max_length=100)

    def  __str__(self):
        return self.Provinces

class CityList(models.Model):
    """
    城市表
    """
    City = models.CharField(max_length=100)
    Province = models.ForeignKey(ProvinceList,on_delete=models.CASCADE)

    def  __str__(self):
        return self.City