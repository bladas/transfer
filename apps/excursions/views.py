from django.views.generic import ListView
from .models import Excursion


class ExcursionView(ListView):
    template_name = 'excursions.html'

    def get_queryset(self):
        return Excursion.objects.all()
