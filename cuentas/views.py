from django.contrib.auth.forms import RegistroUsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.


def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("lista_pokemon")  # Ajusta a tu URL principal
    else:
        form = RegistroUsuarioForm()
    return render(request, "usuarios/registro.html", {"form": form})
