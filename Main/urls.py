from django.urls import path
from . import views

app_name = "Main"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="sobre-mi"),
]
