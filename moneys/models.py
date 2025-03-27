from django.db import models
from users.models import CustomUser

class Folder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='folders')

class AddMoney(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='files')