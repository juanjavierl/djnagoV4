# librerias internos de Python
import datetime
# librerias de Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
#librerias externas para django


# Create your views here.
""" def home(request):
    nombre  = "Juan"
    fecha = datetime.datetime.now()
    datos= {
        'name': 'Jose Pinto',
        'fecha': fecha,
        'edad': 16,
        'celular': '123456789',
    }
    return render(request, 'home.html', {'nombre': nombre, 'fecha': fecha, 'datos': datos}) """



def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirige a la página de inicio después de iniciar sesión
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')

def salir(request):
    logout(request)
    return redirect('home')