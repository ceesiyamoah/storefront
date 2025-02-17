from django.db import models

# Create your models here.


class Promotion (models.Model):
    description = models.TextField()
    discount = models.FloatField()


class Collection (models.Model):
    title = models.CharField(max_length=255)
    featured_products = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


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
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem (models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address (models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=5, null=True)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True)


class Cart (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
