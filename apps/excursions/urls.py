from django.urls import path
from apps.excursions.views import *
app_name = 'excursion'
urlpatterns = [
    path('', ExcursionView.as_view(), name='excursion')
]