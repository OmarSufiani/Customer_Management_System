from django.urls import path
from .import views 

urlpatterns = [
    
    
    path('', views.homePage, name='home'),
    path('login/', views.loginUser, name='login'),
    path('about/', views.about, name='about'),
    path('register/', views.registerUser, name='register'),
    path('base/', views.baseForm, name='base'),
    path('logout/', views.logoutUser, name='logout'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
    
     
]