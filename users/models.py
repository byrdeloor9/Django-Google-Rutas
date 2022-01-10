from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    direccion = models.CharField(verbose_name="Direccion",max_length=100 , null=True,blank=True)
    ciudad = models.CharField(verbose_name="Ciudad",max_length=100 , null=True,blank=True)
    condado = models.CharField(verbose_name="Condado",max_length=100 , null=True,blank=True)
    codigo_postal = models.CharField(verbose_name="Codigo Postal",max_length= 8, null=True,blank=True)
    pais = models.CharField(verbose_name="Pais",max_length= 100, null=True,blank=True)
    longitud = models.CharField(verbose_name="Longitud",max_length=50 , null=True,blank=True)
    latitud = models.CharField(verbose_name="Latitud",max_length= 50, null=True,blank=True)

    puntaje_captcha = models.FloatField(default=0.0)
    perfil_b = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'