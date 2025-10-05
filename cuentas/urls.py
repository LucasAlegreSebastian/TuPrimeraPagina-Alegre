from django.urls import path
from .views import registrar_usuario

app_name = "cuentas"

urlpatterns = [
    path("registro/", registrar_usuario, name="registro"),
]
