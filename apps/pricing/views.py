from django.views.generic import ListView
from .models import *


class PriceView(ListView):
    template_name = 'pricing.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['alikante'] = TransferAlikante.objects.filter()
        context['valensia'] = TransferValencia.objects.filter()
        return context



class Alikante(ListView):
    template_name = 'alikante.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['alikante'] = TransferAlikante.objects.filter()

        return context




class Valensia(ListView):
    template_name = 'valensia.html'

    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['valensia'] = TransferValencia.objects.filter()

        return context