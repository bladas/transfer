from django.urls import path
from apps.orders.views import *
app_name = 'orders'
urlpatterns = [
    path('', Orders.as_view(), name='orders'),
    path('successfully/', Successfully.as_view(), name='successfully')
]