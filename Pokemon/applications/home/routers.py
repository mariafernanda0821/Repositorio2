from rest_framework.routers import DefaultRouter
#
from .import viewsets


router = DefaultRouter()

#router.register(r'colors', viewsets.ColorViewSet, basename= 'colors')  
#router.register(r'productos', viewsets.ProductViewSet, basename= 'productos')  
router.register(r'regions', viewsets.RegionViewSet, basename= 'region') 
router.register(r'locations', viewsets.LocationViewSet, basename= 'location') 
#router.register(r'pokemons', viewsets.PokemonViewSets, basename= 'pokemon_descripcion') 
router.register(r'pokemons/own', viewsets.PokemonCapturadoViewSets, basename= 'pokemon_own') 

#PokemonOwnViewSets


urlpatterns = router.urls
