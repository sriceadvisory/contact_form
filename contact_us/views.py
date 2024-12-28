from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import Contact_Us_Modelform
from django.views.generic.base import TemplateView
from .models import Contact_Us


# Create your views here.
class ContactUsView(View):
    def get(self, request):
        form = Contact_Us_Modelform()

        return render(request, 'contact_us/contact_form.html', {
            "form": form,
        })
    def post(self, request):
        form = Contact_Us_Modelform(request.POST)
        if form.is_valid():
            form.save()# if using model forms you can just add this save line to the code.
            return HttpResponseRedirect("/thank_you")


class ThankYouView(TemplateView):
    template_name = 'contact_us/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This is the message"
        return context

class ContactListView(TemplateView):
    template_name = 'contact_us/contact_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contact_us = Contact_Us.objects.all()
        context["Contact_Us"] = Contact_Us
        return context