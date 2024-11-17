from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer (models.Model):

    MEMEMBERSHIP_BRONZE = 'B'
    MEMEMBERSHIP_SILVER = 'S'
    MEMEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMEMBERSHIP_BRONZE, 'Bronze'),
        (MEMEMBERSHIP_SILVER, 'Silver'),
        (MEMEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMEMBERSHIP_BRONZE)


class Order (models.Model):

    STATUS_PENDING = 'P'
    STATUS_COMPLETE = 'C'
    STATUS_FAILED = 'F'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_COMPLETE, 'Complete'),
        (STATUS_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_PENDING)
