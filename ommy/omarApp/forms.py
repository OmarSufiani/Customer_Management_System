from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


#Create a forms here


        
       #

    #
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')


        
            
        
       # widgets={
              #  'username':forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            #    'password1':forms.TextInput(attrs={'class':'form-control','placeholder':'enter password'}),
              #  'password2':forms.EmailInput(attrs={'class':'form-control','placeholder':'confirm password'}),


      # } 
class Productform(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        #fields=('product_name','price','category','description')


        

class Customerform(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"


class orderform(ModelForm):
    class Meta:
        model=Order
        fields="__all__"

        