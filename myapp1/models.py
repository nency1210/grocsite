from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, date
import math
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(max_length=200, null=True,blank=True)

    def __str__(self):
        return self.name

class Client(User):
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'), ]
    # fullname = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, default='CH', choices=CITY_CHOICES)
    interested_in = models.ManyToManyField(Type)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Client"

class OrderItem(models.Model):
    order_status = [
        ('0' ,'cancelled'),
        ('1','placed_order'),
        ('2','shipped_order'),
        ('3','deliverd_order')]
    ordered_item = models.ForeignKey(Item, related_name='orderedItem', on_delete=models.CASCADE)
    ordered_by = models.ForeignKey(Client, related_name='orderedBy', on_delete=models.CASCADE)
    no_of_order = models.PositiveIntegerField()
    status = models.CharField(max_length=2, default='1', choices=order_status)
    date = models.DateField()

    def __str__(self):
        return self.ordered_item

    def total_price(self):
        sum([item.total_cost for item in Item.objects.filter(name = self.ordered_item)])
        # return sum[(self.ordered_item.price * self.no_of_order)]

class Description(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length=200, null=True,blank=True)
    time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title