# TuPrimeraPagina-Alegre

## Descripción
Proyecto en Django que permite gestionar una **Pokedex** con los siguientes modelos: **Pokemon, Entrenador, Gimnasio y Pokebola**.  
Cada modelo tiene su propia página para listar los registros, buscar y añadir nuevos elementos mediante un dropdown.
**Ahora se suma la funcion de combate**

## Superusuario
- **Usuario:** `admin`  
- **Contraseña:** `admin`
- Solo el Superusuario puede añadir informacion a la base de datos.

## Modelos
##Funcionalidades de agregar solo para Superusuario

### Pokemon
Campos: `numero`, `nombre`, `tipo`, `debilidad`, `habilidad` , `imagen` 
Funcionalidad: listado de Pokemons,detalle, búsqueda y añadido de nuevos Pokemons.

### Entrenador
Campos: `nombre`, `region` , `imagen` 
Funcionalidad: listado de entrenadores, búsqueda y añadido de nuevos entrenadores.

### Gimnasio
Campos: `ciudad`, `lider`,  `imagen` 
Funcionalidad: listado de gimnasios, búsqueda y añadido de nuevos gimnasios.

### Pokebola
Campos: `nombre`, `descripcion` , `imagen`  
Funcionalidad: listado de pokebolas, búsqueda y añadido de nuevas pokebolas.

**NUEVA FUNCION -COMBATE-**
Lo usuarios que esten Logueados en la apgina tienen acceso a una seccion de combate, para poder realizar batallas entre su pokemon favorito (o tambien puede elegir de una lista) contra otros usuarios registrados, pokemon de una lista o tambien uno aleatorio.

##Historial
Se guardaran los combates realizados en un historial general que podran ver todos los usuarios como tambien se filtrará el mismo cuando se accede desde el perfil a su historial personal.

#Perfil
El usuario ve sus estadisticas de combate resumidas, puede cambiar su avatar y elegir su pokemon favorito.

# Instalar dependencias
pip install -r requirements.txt
