from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
    nombre=forms.CharField(max_length=30,required=True,
        widget=forms.TextInput(attrs={'placeholder': "Primer Nombre.."}))
    apellido=forms.CharField(max_length=30,required=True,
        widget=forms.TextInput(attrs={'placeholder': "Primer Nombre.."}))
    usuario=forms.CharField(max_length=30,required=True,
        widget=forms.TextInput(attrs={'placeholder': "Primer Nombre.."}))
    password1= forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Contraseña..','class':'password'}))
    password2= forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Confirmar contraseña..','class':'password'}))

    #Recaptcha Token
    token = forms.CharField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = User
        fields=('usuario','nombre','apellido','password1','password2')

class AuthForm(AuthenticationForm):
    usuario= forms.EmailField(max_length=254, required=True,widget=forms.TextInput(attrs={'placeholder':'Correo'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña','class':'password'}))\
    
    class Meta:
        model = User
        fields=('usuario','password')    

class UserProfileForm(forms.ModelForm):
    direccion = forms.CharField(max_length=100,required=True, widget=forms.HiddenInput())
    ciudad = forms.CharField(max_length=100 , widget=forms.HiddenInput())
    condado = forms.CharField(max_length=100 , widget=forms.HiddenInput())
    codigo_postal = forms.CharField(max_length= 8, widget=forms.HiddenInput())
    pais = forms.CharField(max_length= 100, widget=forms.HiddenInput())
    longitud = forms.CharField(max_length=50, widget=forms.HiddenInput())
    latitud = forms.CharField(max_length= 50, widget=forms.HiddenInput())


    class Meta:
        model = UserProfile
        fields = ('direccion','ciudad','condado','codigo_postal','pais','longitud','latitud')