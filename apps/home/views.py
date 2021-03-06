from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, FormView
from .models import Calculate, Start, Space, TypeCar, OrderCalculates
from .forms import HomeForms, StartForms, KudaForms, TypeCarForms


class HomeView(FormView):
    template_name = 'home.html'
    form_class = HomeForms

    def get_queryset(self):
        return

    def get_context_data(self,**kwargs):
        print('suka da')
        context = super().get_context_data(**kwargs)
        self.request.session['start'] = None
        self.request.session['kuda'] = None
        self.request.session['type_car'] = None
        self.request.session['suma'] = None

        context['starts'] = Start.objects.all()
        context['type_car_forms'] = TypeCarForms
        context['start_forms'] = StartForms
        start_first_el = Start.objects.all().order_by('-id')[0]
        context['kuda_forms'] = KudaForms(start=int(start_first_el.id))

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
        start_first_el = Start.objects.all().order_by('-id')[0]

        kuda_forms = KudaForms(data=request.POST, start=int(start_first_el.id))

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

        if (request.session['start'] != None and request.session['kuda'] != None and request.session[
            'type_car'] != None):
            print("rez")
            filt_start = Start.objects.filter(name=str(request.session['start']))[0]
            filt_kuda = Space.objects.filter(name=str(request.session['kuda']),start=filt_start)[0]
            filt_type_car = TypeCar.objects.filter(name=str(request.session['type_car']))[0]

            price_filter = OrderCalculates.objects.get(start_id=filt_start.id, kuda_id=filt_kuda.id,
                                                       type_car_id=filt_type_car.id)

            request.session['suma'] = price_filter.price
            context['suma'] = request.session['suma']

            request.session['start'] = None
            request.session['kuda'] = None
            request.session['type_car'] = None

            request.session['suma'] = None
            del request.session['start']
            del request.session['kuda']
            del request.session['type_car']
        return render(request, 'home.html', context)
