from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def homeSec(request):
    return render( request, "registro/homeSec.html")

def registraUsario(request):
    if request.method == 'POST':
        formulario =UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')

    else: 
        formulario = UserCreationForm()
    contexto  = {'formulario': formulario,}
    return render(request,'registro/registro.html', contexto)

def paginaProfile(request):
    return render(request, 'registro/paginaProfile.html')