from django import forms

from apps.orders.models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'lastname', 'phone', 'otkuda', 'kuda',
                  'kolichestvo',
                  'data', 'description', 'email','hours','detey')

    def save(self, commit=True):
        new_order = Order.objects.create(
            name=self.cleaned_data['name'],
            lastname=self.cleaned_data['lastname'],
            phone=self.cleaned_data['phone'],
            otkuda=self.cleaned_data['otkuda'],
            kuda=self.cleaned_data['kuda'],
            kolichestvo=self.cleaned_data['kolichestvo'],
            data=self.cleaned_data['data'],
            hours=self.cleaned_data['hours'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            detey=self.cleaned_data['detey']
        )
        return new_order.save()