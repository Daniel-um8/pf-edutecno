from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from .models import ContactMessage
# Create your views here.

# def home(request):
#     return render(request, 'app1/index.html', {})

# def test_base(request):
#     return render(request, 'base.html')

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Crear y guardar el mensaje en la base de datos
            ContactMessage.objects.create(
                nombre=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                mensaje=form.cleaned_data['message']
            )
            
            # Opcional: Retornar una respuesta de éxito
            messages.success(request, "Gracias por tu mensaje. Te contactaremos pronto.")

    else:
        form = ContactForm()

    return render(request, 'app1/index.html', {'form': form})