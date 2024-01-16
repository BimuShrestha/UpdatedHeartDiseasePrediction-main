from django.db import models

class MyModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)