from django.shortcuts import render, redirect

# Create your views here.
from .models import Pokemon
from .forms import PokemonForm


def poke_list(request):
    poke_list = Pokemon.objects.all()
    return render(request, "pokedex/pokemon_list.html", context={"pokemon": poke_list})


def poke_crear(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            Pokemon = form.save(commit=False)
            if request.user.is_authenticated:
                Pokemon.autor = request.user
                Pokemon.save()
                return redirect("pokedex:list_pokemon")
            else:
                form.add_error(None, "Deber loguearte")
    else:
        form = PokemonForm()
    return render(request, "pokedex/pokemon_crear.html", context={"form": form})
