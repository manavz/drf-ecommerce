from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("address", views.CustomerAddressViewset)
router.register("productrating", views.ProductRatingViewset)


urlpatterns = [
    path("vendors/", views.VendorList.as_view()),
    path("vendor/<int:pk>/", views.VendorDetail.as_view()),
    # Categories
    # Products
    path("products/", views.ProductList.as_view()),
    path("product/<int:pk>/", views.ProductDetail.as_view()),
    # Customers
    path("customers/", views.CustomerList.as_view()),
    path("customer/<int:pk>/", views.CustomerDetail.as_view()),
    # Orders
    path("orders/", views.OrderList.as_view()),
    path("order/<int:pk>/", views.OrderDetail.as_view()),
]

urlpatterns += router.urls
