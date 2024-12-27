from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import contact_us_form
from .models import Contact_Us


# Create your views here.
def contact_us(request):
    if request.method == "POST":
        form = contact_us_form(request.POST)

        if form.is_valid():
           contact = Contact_Us(user_name=form.cleaned_data['user_name'],
                                email=form.cleaned_data['email'],
                                contact_message=form.cleaned_data['contact_message'
                                ])
           #if using model forms you can just add this save line to the code.
           contact.save()
        return HttpResponseRedirect("/thank_you")
    else:
        form = contact_us_form()

    return render(request, 'contact_us/contact_form.html', {
            "form": form,
        })


def thank_you(request):
    return render(request, "contact_us/thank_you.html")