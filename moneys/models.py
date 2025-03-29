from django.db import models
from users.models import CustomUser

class Folder(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='folders')
    
    def __str__(self):
        return self.name

class AddMoney(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    valuta = models.CharField(max_length=10, default='USD')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='files')
    
    def __str__(self):
        return f'{self.name} - {self.folder.name}'