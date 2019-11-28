from django.shortcuts import redirect, render

from apps.contact.forms import Contactform


def Contact(request):
    form = Contactform()
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)

            inst.save()
            return redirect(request.path)

    context = {

        'form': form,

    }
    return render(request, 'contact.html', context)
