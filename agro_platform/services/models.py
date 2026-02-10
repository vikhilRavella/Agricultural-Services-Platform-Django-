from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Fertilizer(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    supplier = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_wage = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Booking(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
class Product(models.Model):
    supplier = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farmer_orders')
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=30, default='Pending')
class ProviderEquipment(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)


class ProviderWorker(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    daily_wage = models.DecimalField(max_digits=8, decimal_places=2)
