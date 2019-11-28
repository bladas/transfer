from django import forms

from .models import Calculate


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
