from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage # Sirve para crear la estructura de un mensaje e incluye un método para enviarlo
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm() # Creamos la plantilla vacía

    if request.method == "POST": # Detectamos si se envió algún dato por POST
        contact_form = ContactForm(data=request.POST) # Si se envió, rellenamos la plantilla con esa información
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["paulasofiasingh@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                # Todo salió bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no salió bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html',{'form':contact_form})