from django import forms

from apps.orders.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'phone', 'otkuda', 'kuda',
                  'kolichestvo',
                  'data', 'description', 'email','detey','deteydescr')

    def save(self, commit=True):
        new_order = Order.objects.create(
            name=self.cleaned_data['name'],
            phone=self.cleaned_data['phone'],
            otkuda=self.cleaned_data['otkuda'],
            kuda=self.cleaned_data['kuda'],
            kolichestvo=self.cleaned_data['kolichestvo'],
            data=self.cleaned_data['data'],

            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            detey=self.cleaned_data['detey'],
            deteydescr=self.cleaned_data['deteydescr']
        )
        return new_order.save()