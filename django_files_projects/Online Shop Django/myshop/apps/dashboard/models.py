from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



categories=(('laptops','Laptops'),('phones','Phones'),
            ('gadgets','Gadgets'))

class ProductModel(models.Model):
    product_name=models.CharField(max_length=233, db_index=True)
    category=models.CharField(max_length=60, choices=categories, default='laptops')
    slug=models.SlugField(max_length=233, db_index=True)
    image_product=models.ImageField(upload_to='products', blank=True)
    specifications=models.CharField(max_length=100, blank=True)
    about_product=models.TextField(blank=True)
    available=models.BooleanField(default=True,editable=True)
    price=models.DecimalField(max_digits=10, decimal_places=2, editable=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)


    class Meta:
        ordering=('product_name',)
        index_together=(('id','slug'),) 


        

    

class OrderModel(models.Model):
    name_product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    client_name=models.ForeignKey(User, on_delete=models.CASCADE)
    qty_ordered=models.PositiveIntegerField()
    time_of_order=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.client_name} => {self.name_product}'



