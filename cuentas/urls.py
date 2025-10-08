from django.urls import path
from .views import (
    registrar_usuario,
    editar_perfil,
    perfil,
    login_usuario,
    logout_usuario,
    cambiar_contraseña,
)

app_name = "cuentas"

urlpatterns = [
    path("registro/", registrar_usuario, name="registro"),
    path("editar-perfil/", editar_perfil, name="editar-perfil"),
    path("perfil/", perfil, name="perfil"),
    path("login/", login_usuario, name="login"),
    path("logout/", logout_usuario, name="logout"),
    path("cambiar-contraseña/", cambiar_contraseña, name="cambiar_contraseña"),
]
