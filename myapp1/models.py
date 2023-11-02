from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

 # Creating a model called 'Type'.
class Type(models.Model):
    name = models.CharField(max_length=200)

    # Defining an str method to return name of each type.
    def __str__(self):
        return self.name

# Creating a model called 'Item' which has a foreign key referencing 'Type' model.
class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    # Defining an str method to return name of each item.
    def __str__(self):
        return self.name

# Creating a model called 'Client' having a many to many relation with 'Type' model.
class Client(User):
    CITY_CHOICES = [('WD', 'Windsor'), ('TO','Toronto'), ('CH', 'Chatham'), ('WL', 'Waterloo')]
    #fullname = models.CharField(max_length=50, null=True, blank=True)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type,null=True, blank=True)

    # Defining an str method to return first and last name of each client.
    def __str__(self):
        return self.first_name + ' ' + self.last_name
        #return self.fullname

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

# Creating a model called 'OrderItem' which has 2 foreign keys referencing 'Item' and 'Client' models.
class OrderItem(models.Model):
    item = models.ForeignKey(Item, related_name='orders', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='client', on_delete=models.CASCADE)
    units = models.PositiveIntegerField()
    STATUS_CHOICES = [('0','Cancelled'), ('1','Successful'), ('2','Shipped'), ('3','Delivered')]
    status = models.CharField(max_length=50,choices=STATUS_CHOICES)
    order_date = models.DateTimeField(auto_now=True)

    # Defining an str method to return type of each item.
    def __str__(self):
        return self.item.name

    # Calculating the total price of the order placed by the client
    def _get_total(self):
        return (self.units * self.item.price)

    total_price = property(_get_total)