from django.urls import path
from apps.contact import views
app_name = 'contact'
urlpatterns = [
    path('', views.Contact, name='contact')
]