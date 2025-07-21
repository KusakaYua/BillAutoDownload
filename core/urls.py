from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-billing-site/', views.add_billing_site, name='add_billing_site'),
    path('bill-management/', views.bill_management, name='bill_management'),
]
