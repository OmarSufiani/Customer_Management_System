from django.db import models

# Create your models here.





      
class Customer(models.Model):
    NATIONALITY=(
               ('Kenya','Kenya'),
               ('Uganda','Uganda'),
               ('Tanzania','Tanzania'),
               )
        
    name=models.CharField(max_length=50,null=False)
    contacts=models.CharField(max_length=100,null=False)
    email=models.EmailField(max_length=100 )
    address=models.CharField(max_length=100, blank=True)
    nationality=models.CharField(max_length=50, null=True, choices=NATIONALITY)
    
    #new_field=models.CharField(max_length=200, default='DEFAULT VALUE', blank=True, null=True)
    def __str__(self):
        return self.name    


class Order(models.Model):
    ITEM=(
         ('SHOES','SHOES'),
         ('FLASH','FLASH'),
         ('PHONE','PHONE'),
         ('CHARGER','CHARGER'),
         ('EXTENSION','EXTENSION'),
         ('EARPHONES','EARPHONES'),
         ('BLUETOOTH','BLUETOOTH'),
         ('SPEAKER','SPEAKER'),
         )

    ORDER=(
         ('YES','YES'),
         ('NO','NO'),
         )
    item=models.CharField(max_length=100, null=False, choices=ITEM)
    order=models.CharField(max_length=50, blank=False, choices=ORDER)

    def __str__(self):
        return self.item







class Product(models.Model):


    #
    CATEGORY=(
            ('local','local'),
            ('ugandan','ugandan'),
            ('foreign','foreign'),
            )
    product=models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    price=models.CharField(max_length=100,null=False, blank=True)
    category=models.CharField(max_length=100, choices=CATEGORY)
    description=models.CharField(max_length=100, blank=True)
    
    def __str__(self):
         return self.product.item


