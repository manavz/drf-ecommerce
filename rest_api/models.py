from django.db import models
from django.contrib.auth.models import User


# Vendor Models
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.username


# product Category
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name="product_category",
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mobile = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customers_orders"
    )
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer)


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class CustomerAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer_adddress"
    )
    address = models.TextField()
    default_address = models.BooleanField(default=False)


class ProductRating(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="rating_customers"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_ratings"
    )
    rating = models.IntegerField()
    reviews = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} - {self.reviews}"
