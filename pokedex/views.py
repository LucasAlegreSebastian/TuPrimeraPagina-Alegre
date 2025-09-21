from django.shortcuts import render

# Create your views here.
from .models import Pokemon


def poke_list(request):
    poke_list = Pokemon.objects.all()
    return render(request, "pokedex/pokemon_list.html", context={"pokemon": poke_list})
