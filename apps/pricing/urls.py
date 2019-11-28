from django.urls import path
from apps.pricing.views import *
app_name = 'pricing'
urlpatterns = [
    path('', PriceView.as_view(), name='pricing')
]