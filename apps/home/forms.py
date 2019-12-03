from django import forms

from .models import Calculate, Space, Start


class HomeForms(forms.ModelForm):
    class Meta:
        model = Calculate
        fields = ['start', 'type_car', 'kuda']

    def save(self, commit=True):
        new_calculate = Calculate.objects.create(
            start=self.cleaned_data['start'],
            type_car=self.cleaned_data['type_car'],
            kuda=self.cleaned_data['kuda'],

        )
        return new_calculate.save()


class StartForms(forms.ModelForm):
    class Meta:
        model = Calculate
        fields = ['start', ]



class TypeCarForms(forms.ModelForm):
    class Meta:
        model = Calculate
        fields = ['type_car', ]


class KudaForms(forms.ModelForm):
    class Meta:
        model = Calculate
        fields = ['kuda', ]

    def __init__(self, start,  *args, **kwargs):
        super(KudaForms, self).__init__(*args, **kwargs)

        if (start != None):
            el_start = Start.objects.filter(pk=int(start))[0]
        else:
            el_start = Start.objects.filter(pk=int(1))[0]
        self.fields['kuda'].queryset = Space.objects.filter(start=el_start)