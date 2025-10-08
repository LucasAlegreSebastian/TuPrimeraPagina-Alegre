from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, EditProfileForm, PasswordChangeForm


def registrar_usuario(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("pokedex:list_pokemon")
    else:
        form = RegistroUsuarioForm()
    return render(request, "cuentas/registro.html", {"form": form})


def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            messages.success(request, f"¡Bienvenido {usuario.username}!")
            return redirect("pokedex:list_pokemon")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "cuentas/login.html")


@login_required
def logout_usuario(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("cuentas:login")


@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("cuentas:perfil")
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, "cuentas/editar-perfil.html", {"form": form})


@login_required
def perfil(request):
    return render(request, "cuentas/perfil.html")


@login_required
def cambiar_contraseña(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(
                request, user
            )  # Para no cerrar sesión automáticamente
            messages.success(request, "Contraseña cambiada correctamente")
            return redirect("cuentas:perfil")
        else:
            messages.error(request, "Por favor corrige los errores")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "cuentas/cambiar_contraseña.html", {"form": form})
