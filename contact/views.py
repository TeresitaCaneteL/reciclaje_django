from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from .forms import  ContactForm
from django.views.generic.edit import CreateView
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
  contact_form= ContactForm()
  if contact_form.is_valid():
    name = request.POST.get('name','')
    email = request.POST.get('email','')
    content = request.POST.get('content','')

    email = EmailMessage(
      "Via Verde: Mensaje de contacto",
      "De {} <{}>\n\nEscribio_\n\n{}".format(name, email,content),
      "no-contestar@inbox.mailtrap.oi"
      ["t.canette@gmail.com"],
      reply_to=[email]
    )
    try:
       email.send()
    except:
       return redirect(reverse('contact')+"?ok")

  return render(request, 'contact.html', {'form':contact_form})
