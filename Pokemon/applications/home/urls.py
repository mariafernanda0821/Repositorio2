"""Pokemon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views, cargarBD


app_name = "home_app"

urlpatterns = [
    path("region/", cargarBD.Cargar_Region, name = "cargar_region"), 
    path("localidad/", cargarBD.Cargar_Localidad, name = "cargar_pokemon"), 
    path("pokemon/", cargarBD.Cargar_Pokemon, name = "cargar_pokemon"), 
    path("area/", cargarBD.Cargar_Area, name = "cargar_area"), 
    #==============******==============

    path(
        'pokemonsA/<pk>/', #​ ['GET'​] /pokemons/<int:pk>/
        views.DescripcionPokemon.as_view(),
        name= 'pokemon_descripcion', 
    ), 

    path(
        #'capturar-pokemon/',  #[​'POST'​] /pokemons/own/
        'pokemons/own/', 
        views.CapturarPokemon.as_view(),
        name = 'capturar_pokemon',
    ),

    path(
        #'mostrar-pokemon-capturado/', #[​'GET'​] /pokemons/own/
        'pokemons2/own/', 
        views.MostrarPokemonCapturados.as_view(),
        name= 'mostrar_pokemon_capturado',
    ),

    path(
        'mostrar-pokemon-capturado-link/', #[​'GET'​] /pokemons/own/
        views.MostrarPokemonCapturadosPorLink.as_view(),
        name= 'mostrar_pokemon_capturado_link',
    ),

    path(
        'pokemonsA/own/<int:pk>/', #[​ 'PUT'​ , ​ 'PATCH'​ ] /pokemons/own/<int:pk>/ UpdateAPIView
        views.AlmacenPokemonUpdateView.as_view(),
        name= 'update_almace_pokemon'
        ),
    path(
        'delete/<int:pk>/', #[​ 'PUT'​ , ​ 'PATCH'​ ] /pokemons/own/<int:pk>/delete
        views.DeletePokemon.as_view(),
        name= 'habilidad2'
        ),

    path(
        'regionsA/', #[​ 'GET'​ ] /regions/
        views.DetailRegiones.as_view(),
        name= 'listar_regiones'
    ),

    path(
        'regionsA/<pk>/', #[​ 'GET'​ ] /regions/<pk>
        views.DetailRegionLocation.as_view(),
        name= 'listar_regiones_location'
    ),

    path(
        'locationsA/<pk>/', #[​ 'GET'​ ] /locations/<pk>
        views.DetailLocations.as_view(),
        name= 'listar_locations'
    ),

    path(
        'areasA/<pk>/', #[​ 'GET'​ ] /areas/<int:pk>/
        views.DetailArea.as_view(),
        name= 'listar_locations'
        ),
]