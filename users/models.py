from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

class Gender(models.TextChoices):
    MALE = ('male', 'Male')
    FEMALE = ('female', 'Female')
    NOSELECT = ('no_select', 'No Select')

class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True, 
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
        default=Gender.NOSELECT
    )