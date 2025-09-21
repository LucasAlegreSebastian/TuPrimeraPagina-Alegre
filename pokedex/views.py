from django.shortcuts import render, redirect

# Create your views here.
from .models import Pokemon, Entrenador, Gimnasio, Pokebola
from .forms import PokemonForm, EntrenadorForm, GimnasioForm, PokebolaForm


def poke_list(request):
    """
    Lista de Pokemon
    """
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        poke_list = Pokemon.objects.filter(nombre__icontains=busqueda)
    else:
        poke_list = Pokemon.objects.all()
    return render(request, "pokedex/pokemon_list.html", context={"pokemon": poke_list})


def entrenador_list(request):
    """
    Lista de entrenadores
    """
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        entrenador_list = Entrenador.objects.filter(nombre__icontains=busqueda)
    else:
        entrenador_list = Entrenador.objects.all()
    return render(
        request, "pokedex/entrenador_list.html", context={"entrenador": entrenador_list}
    )


def poke_crear(request):
    """
    Para añadir pokemon
    """
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)
            if request.user.is_authenticated:
                pokemon.save()
                return redirect("pokedex:list_pokemon")
            else:
                form.add_error(None, "Deber loguearte")
    else:
        form = PokemonForm()
    return render(request, "pokedex/pokemon_crear.html", context={"form": form})


def entrenador_crear(request):
    """
    Para añadir entrenador
    """
    if request.method == "POST":
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            entrenador = form.save(commit=False)
            if request.user.is_authenticated:
                entrenador.save()
                return redirect("pokedex:list_entrenador")
            else:
                form.add_error(None, "Deber loguearte")
    else:
        form = EntrenadorForm()
    return render(request, "pokedex/entrenador_crear.html", context={"form": form})
