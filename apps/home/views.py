from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, FormView
from .models import Calculate
from .forms import HomeForms


class HomeView(FormView):
    template_name = 'home.html'
    form_class = HomeForms

    def get_queryset(self):
        return



    def post(self, request, *args, **kwargs):

        calculate_form = HomeForms(request.POST)

        if calculate_form.is_valid():

            print(calculate_form.data.get('start'))
            print(calculate_form.data.get('kuda'))
            print(calculate_form.data.get('type_car'))
            context = super().get_context_data(**kwargs)
            context['calculator'] = Calculate.objects.filter(start=calculate_form.data.get('start'), kuda=calculate_form.data.get('kuda'),
                                     type_car=calculate_form.data.get('type_car'))

            return render(request,'home.html',context)
        else:
            print(calculate_form.errors)
        print("0")
