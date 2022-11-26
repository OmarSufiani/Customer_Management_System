from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import *
from .forms import *
from django.contrib import messages





def loginUser(request):
    #form=CreateUserForm
    if request.method=='POST':
        username= request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
         
        if user is not None:
            login(request, user)
            return redirect( 'home')
        else:
            messages.info(request,'username OR password is incorect')
            
    context={}
    return render(request, 'login.html',context)



@login_required(login_url='login')
def homePage(request):
    products=Product.objects.all()
    customers=Customer.objects.all()
    orders=Order.objects.all()

    context={'products':products, 'customers':customers, 'orders':orders}
    return render(request, 'home.html',context)  

@login_required(login_url='login')   
def about(request):
    return render(request, 'about.html')

def logoutUser(request) :
    logout(request) 
    return redirect('login')

@login_required(login_url='login')    
def baseForm(request):
    return render(request, 'base.html')


def registerUser(request):
    form=CreateUserForm()
    if request.method=='POST':
         form=CreateUserForm(request.POST)
         if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created ' + user)
            return redirect('login')
         
    return render(request, 'register.html',{'form':form})

@login_required(login_url='login')
def product(request):
    form=Productform
    if request.method=='POST':
         form=Productform(request.POST)
         if form.is_valid():
            form.save()
            messages.info(request,'Details saved successfully!!!')
            return redirect('product')
         
    return render(request, 'product.html',{'form':form})



@login_required(login_url='login')
def order(request):
    form=orderform
       # submitted=True
    if request.method=='POST':
       form=orderform(request.POST)
       if form.is_valid():
          form.save()
          return redirect('order')

    return render(request, 'order.html', {'form':form})
