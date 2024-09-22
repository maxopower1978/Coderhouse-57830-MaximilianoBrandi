from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares/', null=True, blank=True) 
    
    def __str__(self): # Asegúrate de que el upload_to sea 'avatares/'
        return f"{self.user} - {self.image}"
