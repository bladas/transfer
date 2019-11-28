from django.views.generic import ListView
from .models import Service


class ServicesView(ListView):
    template_name = 'services.html'

    def get_queryset(self):
        return Service.objects.all()
