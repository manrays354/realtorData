from django.db import models

# Create your models here.
class Region(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
       return self.name


class Agent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    agency = models.CharField(max_length=100)
    sales = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='agents')

    def __str__(self):
        return f"{self.name} ({self.region.name})"