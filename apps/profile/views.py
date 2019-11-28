from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from apps.orders.models import *
from django.core import mail
from django.template.loader import render_to_string

conection = mail.get_connection()
conection.open()


class ProfileView(ListView):
    template_name = 'profile.html'
    model = Order

    # paginate_by = 5
    def get_queryset(self):
        pass

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['OrderFalse'] = Order.objects.filter(end=False).order_by('-id')
        context['OrderTrue'] = Order.objects.filter(end=True).order_by('-id')
        return context

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        if self.request.method == "POST":
            order_id = self.request.POST.get('order_id')

            objects = Order.objects.get(pk=order_id)

            print(objects.email)
            email = objects.email
            message = render_to_string('message/positive_message.html', {})
            message2 = render_to_string('message/negative_message.html', {})
            if self.request.POST.get('materialExampleRadios') == '1':
                # Order.objects.update(end=True)
                Order.objects.filter(pk=order_id).update(flag = 'Одобрено', end=True)

                with mail.get_connection() as connection:
                    msg =  mail.EmailMessage(
                        'Заказ трансфера по испанни', message,
                        'daskevichvladislav25@gmail.com', [email],
                        connection=connection,
                    )
                    msg.content_subtype = "html"
                    msg.send()
                print("Отправлено одобрение")
                return redirect('/')

            elif self.request.POST.get('materialExampleRadios') == '2':
                # Order.objects.update()
                # Order.objects.update(flag = 'Отклонено')

                Order.objects.filter(pk=order_id).update(flag = 'Отклонено',end=True)


                with mail.get_connection() as connection:
                    msg = mail.EmailMessage(
                        'Заказ трансфера по испанни', message2,
                        'daskevichvladislav25@gmail.com', [email],
                        connection=connection,
                    )
                    msg.content_subtype = "html"
                    msg.send()
                print("Отправлено отказ")
                return redirect('/')