from rest_framework import serializers
from .models import (
    Vendor,
    Product,
    Customer,
    Order,
    OrderItems,
    CustomerAddress,
    ProductRating,
)


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "user", "address"]

    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "user", "address"]

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class ProductListSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "vendor",
            "title",
            "detail",
            "price",
            "product_ratings",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "vendor",
            "title",
            "detail",
            "price",
            "product_ratings",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "user", "mobile"]

    def __init__(self, *args, **kwargs):
        super(CustomerListSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "user", "mobile"]

    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "customer"]

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ["id", "order", "product"]

    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = ["id", "customer", "address", "default_address"]

    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = [
            "id",
            "customer",
            "product",
            "rating",
            "reviews",
            "add_time",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductReviewSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1
