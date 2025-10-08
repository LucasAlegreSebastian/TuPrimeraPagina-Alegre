from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

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


def poke_crear(request):
    """
    Para añadir pokemon
    """
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.save()
            return redirect("pokedex:list_pokemon")
        else:
            form.add_error(None, "Deber loguearte")
    else:
        form = PokemonForm()
    return render(request, "pokedex/pokemon_crear.html", context={"form": form})


class PokemonCreateView(CreateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "pokedex/pokemon_crear.html"
    success_url = reverse_lazy("pokedex:list_pokemon")


class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = "pokedex/pokemon_detalle.html"
    context_object_name = "pokemon"


class PokemonUpdateView(UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "pokedex/pokemon_editar.html"

    def get_success_url(self):
        return reverse_lazy("pokedex:detalle_pokemon", kwargs={"pk": self.object.pk})


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


def entrenador_crear(request):
    """
    Para añadir entrenador
    """
    if request.method == "POST":
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            entrenador = form.save(commit=False)
            entrenador.save()
            return redirect("pokedex:list_entrenador")
        else:
            form.add_error(None, "Deber loguearte")
    else:
        form = EntrenadorForm()
    return render(request, "pokedex/entrenador_crear.html", context={"form": form})


def gimnasios_list(request):
    """
    Lista de Gimnasios
    """
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        gimnasios_list = Gimnasio.objects.filter(nombre__icontains=busqueda)
    else:
        gimnasios_list = Gimnasio.objects.all()
    return render(
        request, "pokedex/gimnasio_list.html", context={"gimnasios": gimnasios_list}
    )


def gimnasio_crear(request):
    """
    Para añadir gimnasio
    """
    if request.method == "POST":
        form = GimnasioForm(request.POST)
        if form.is_valid():
            gimnasio = form.save(commit=False)
            gimnasio.save()
            return redirect("pokedex:list_gimnasios")
        else:
            form.add_error(None, "Error")
    else:
        form = GimnasioForm()
    return render(request, "pokedex/gimnasio_crear.html", context={"form": form})


def pokebolas_list(request):
    """
    Lista de Pokebolas
    """
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        pokebolas_list = Pokebola.objects.filter(nombre__icontains=busqueda)
    else:
        pokebolas_list = Pokebola.objects.all()
    return render(
        request, "pokedex/pokebolas_list.html", context={"pokebolas": pokebolas_list}
    )


def pokebola_crear(request):
    """
    Para añadir pokebolas
    """
    if request.method == "POST":
        form = PokebolaForm(request.POST)
        if form.is_valid():
            pokebola = form.save(commit=False)
            pokebola.save()
            return redirect("pokedex:list_pokebolas")
        else:
            form.add_error(None, "error")
    else:
        form = PokebolaForm()
    return render(request, "pokedex/pokebola_crear.html", context={"form": form})
