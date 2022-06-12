from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

# Create your models here.

# Customer model 
class Customer(models.Model):
    name=models.CharField(max_length=20,null=True)
    phone=models.CharField(max_length=10,null=True)
    place=models.CharField(max_length=20,blank=True)
    email=models.EmailField(blank=True)

    def __str__(self):
        return self.name 

# Workers model
class Worker(models.Model):
    name=models.CharField(max_length=15,null=True)
    phone=models.CharField(max_length=10,null=True)
    place=models.CharField(max_length=20,null=True)
    email=models.EmailField(blank=True)

    def __str__(self):
        return self.name

# product model
class Product(models.Model):
    name=models.CharField(max_length=15,null=True)
    price=models.IntegerField(null=True)

    def __str__(self):
        return self.name

# Stock model
class Stock(models.Model):
    name=models.CharField(max_length=20,null=True)
    quantity=models.IntegerField(null=True)

    def __str__(self):
        return self.name
# Order modl
class Order(models.Model):
    status=(
        ('Delivered','Delivered'),
        ('Not-Delivered','not-Delivered'),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_cretated=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,null=True,choices=status)

    def __str__(self):
        return self.customer.name

# Bill model
class Bill(models.Model):
    bill_num=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=20,null=True)
    products=models.ManyToManyField('bill_product')
    total_sum=models.FloatField(default=2.0)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('bill-detail',args=[str(self.bill_num)])

    def add_product(self):
        return reverse('add-bill-product',args=[str(self.bill_num)])

# Bill product model
class bill_product(models.Model):
    bill_product_num=models.AutoField(primary_key=True)
    bill_item=models.ForeignKey('bill',on_delete=models.SET_NULL,null=True)
    billprod=models.ForeignKey('product',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1,help_text='default is 1')


def __str__(self):
    return self.billprod.product_name


# Expense model
class Expense(models.Model):
    travel=models.IntegerField(blank=True)
    purchase=models.IntegerField(blank=True)
    others=models.IntegerField(blank=True)
    date=models.DateTimeField(auto_now_add=True)

# Income model

class Income(models.Model):
    customer=models.CharField(max_length=20,null=True)
    amount=models.IntegerField(null=True)