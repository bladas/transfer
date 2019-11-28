from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, render_to_response
from django.views.generic import ListView, FormView, UpdateView

from apps.orders.forms import OrderForm
from apps.orders.models import Order


class Orders(FormView):
    template_name = 'order.html'
    form_class = OrderForm
    success_url = '/successfully/'
    model = Order

    def post(self, request, *args, **kwargs):

        bound_form = OrderForm(request.POST)

        if bound_form.is_valid():

            bound_form.save()

            return redirect('successfully/')
        else:
            print(bound_form.errors)

        return render(request, 'order.html', context={'form': bound_form})


class Successfully(ListView):
    template_name = 'successfully.html'

    def get_queryset(self):
        pass
