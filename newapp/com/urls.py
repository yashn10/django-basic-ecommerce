from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('contact/', views.contact, name="Contact"),
    path('about/', views.about, name="About"),
    path('search/', views.search, name="Search"),
    path('productdetail/<int:id>', views.productdetail, name="Productdetail"),
    path('checkout/', views.checkout, name="Checkout"),
]