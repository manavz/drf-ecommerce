from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models
from rest_framework import viewsets


class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_class = [IsAuthenticated]


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    # permission_class = [IsAuthenticated]


class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer
    # permission_class = [IsAuthenticated]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
    # permission_class = [IsAuthenticated]


class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerListSerializer
    # permission_class = [IsAuthenticated]


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerDetailSerializer
    # permission_class = [IsAuthenticated]


class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    # permission_class = [IsAuthenticated]


class OrderDetail(generics.ListCreateAPIView):
    # queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderDetailSerializer
    # permission_class = [IsAuthenticated]

    def get_queryset(self):
        order_id = self.kwargs["pk"]
        order = models.Order.objects.get(id=order_id)
        print(order)
        order_items = models.OrderItems.objects.filter(order=order)
        return order_items


class CustomerAddressViewset(viewsets.ModelViewSet):
    queryset = models.CustomerAddress.objects.all()
    serializer_class = serializers.CustomerAddressSerializer


class ProductRatingViewset(viewsets.ModelViewSet):
    queryset = models.ProductRating.objects.all()
    serializer_class = serializers.ProductReviewSerializer
