from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, FormView
from .models import Calculate
from .forms import HomeForms


class HomeView(FormView):
    template_name = 'home.html'
    form_class = HomeForms

    def get_queryset(self):
        return

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['calculate'] = get_object_or_404(Calculate, pk=1)
        return context

    def post(self, request, *args, **kwargs):
        calculate_form = HomeForms(request.POST)

        Calculate.objects.filter().update(price=None)
        if (calculate_form.data.get('start') == '1'):
            if (calculate_form.data.get('type_car') == '1'):
                if (calculate_form.data.get('kuda') == '1'):
                    Calculate.objects.filter().update(price='60')
                    print('super')

        if calculate_form.is_valid():

            return redirect('/')
        else:
            print(calculate_form.errors)
        print("0")
