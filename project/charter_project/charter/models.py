from django.db import models


class DataBase(models.Model):
    region = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.region
