from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, FormView
from .models import Calculate, Start, Space, TypeCar,OrderCalculates
from .forms import HomeForms, StartForms, KudaForms, TypeCarForms


class HomeView(FormView):
    template_name = 'home.html'
    form_class = HomeForms

    def get_queryset(self):
        return

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['starts'] = Start.objects.all()
        context['type_car_forms'] = TypeCarForms
        context['start_forms'] = StartForms
        context['kuda_forms'] = KudaForms(start=1)
        return context

    def post(self, request, *args, **kwargs):

        context = super().get_context_data(**kwargs)

        start = ''
        type_car = ''
        kuda = ''
        suma = ''

        try:
            start = request.session['start']
            kuda = request.session['kuda']
            type_car = request.session['type_car']
            suma = request.session['suma']

        except:
            request.session['start'] = None
            request.session['kuda'] = None
            request.session['type_car'] = None
            request.session['suma'] = None

        # request.session['start'] = None
        # request.session['kuda'] = None
        # request.session['type_car'] = None

        #
        print('******************************')

        start_form = StartForms(request.POST)
        type_car_form = TypeCarForms(request.POST)
        kuda_forms = KudaForms(data=request.POST, start=1)

        if start_form.data.get('start') != None:
            if start is None:
                print("Zapovniv 1")
                start = Start.objects.get(pk=start_form.data.get('start'))
                request.session['start'] = start.name

        if kuda_forms.data.get('kuda') != None:
            if kuda is None:
                print("Zapovniv 2")
                space = Space.objects.get(pk=start_form.data.get('kuda'))
                request.session['kuda'] = space.name

        if type_car_form.data.get('type_car') != None:
            if type_car is None:
                print("Zapovniv 3")
                type_car = TypeCar.objects.get(pk=start_form.data.get('type_car'))
                request.session['type_car'] = type_car.name



        context['start_forms'] = StartForms()
        context['kuda_forms'] = KudaForms(start=start_form.data.get('start'))
        context['type_car_forms'] = TypeCarForms()


        context['start'] = request.session['start']
        context['kuda'] = request.session['kuda']
        context['type_car'] = request.session['type_car']



        if (request.session['start'] != None and request.session['kuda'] != None and request.session['type_car'] != None):
            price_filter = OrderCalculates.objects.filter(start = start_form.data.get('start'),kuda = kuda_forms.data.get('kuda'),type_car = type_car_form.data.get('type_car') )
            request.session['suma'] = price_filter
            context['suma'] = request.session['suma']

            request.session['start'] = None
            request.session['kuda'] = None
            request.session['type_car'] = None

            request.session['suma'] = None

        return render(request, 'home.html', context)

        # calculate_form = HomeForms(request.POST)
        #
        # if calculate_form.is_valid():
        #
        #     print(calculate_form.data.get('start'))
        #     print(calculate_form.data.get('kuda'))
        #     print(calculate_form.data.get('type_car'))
        #     if calculate_form.data.get('start') != '1':
        #         # err = calculate_form.errors['Выберите Аеропорт']
        #         # print(calculate_form.error_message)
        #         context = super().get_context_data(**kwargs)
        #         context['calculator'] = Calculate.objects.filter(start=calculate_form.data.get('start'), kuda=calculate_form.data.get('kuda'),
        #                                  type_car=calculate_form.data.get('type_car'))
        #         # context['err'] = err
        #
        #         return render(request,'home.html',context)
        # else:
        #     print(calculate_form.errors)
        # print("0")
