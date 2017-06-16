from django.db import models


class Client(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    balance = models.FloatField()
    user_password = models.IntegerField()


