from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.template import Template, Context
from .models import Services

# Create your views here.
class ServicesView(View):
  def get(self, request, *args, **kwargs):
    services = Services.objects.all()
    context={
      'services':services

     }
    return render(request, 'services.html', context)





