from django.urls import path
from apps.pricing.views import *
app_name = 'pricing'
urlpatterns = [
    path('', PriceView.as_view(), name='pricing'),
    path('alikante/', Alikante.as_view(), name='alikante'),
    path('valencia/', Valensia.as_view(), name='valencia'),
]