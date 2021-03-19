from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import(
    ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView,  ListCreateAPIView,
    DestroyAPIView, RetrieveDestroyAPIView,
)
# serielizers
from .serializers import(
    PokemonDescripcionSerializer, CapturarPokemomSerializer, PokemonCapturadoSerializer, PagSerializer,
    PokemonCapturadoPorLinkSerializer, RegionSerializer, RegionLocationSerializer,DetallarLocationsSerializer,
    DetailAreaSerializer, HabilidadSerializer,UpdateAlmacenPokemon
)
#models
from .models import (
    Pokemon, AlmacenPokemonCapturado, Region , Location, Area, Habilidades,

)

#VISTA DE DESCRIPCION DE CADA POKEMON QUE INDIUES
class DescripcionPokemon(ListAPIView):

    serializer_class = PokemonDescripcionSerializer

    def get_queryset(self):
        
        pokemon_id = self.kwargs['pk'] 

        return Pokemon.objects.detalles_pokemon(pokemon_id)


#VISTA DE CAPTURAR UN POKEMON
class CapturarPokemon(CreateAPIView):

    serializer_class = CapturarPokemomSerializer

    def create(self, request , *args, **kwargs):

        serializer = self.serializer_class(data= request.data)

        serializer.is_valid(raise_exception=True) 

        #recuperar_pokemon_id = serializer.validated_data["specie"]
       
        pokemon_id = Pokemon.objects.get(id =serializer.validated_data["specie"])
        #recuperar_usuario = serializer.validated_data["nick_name"]
    
        if AlmacenPokemonCapturado.objects.contar_usuario(serializer.validated_data["nick_name"]) > 7:
            
            return Response("Usuario tiene el limite de pokemon capturado")

        else:
            
            capturar_pokemon = AlmacenPokemonCapturado.objects.capturar_pokemon(serializer, pokemon_id)
            capturar_pokemon.save()

            return Response ( 
                {
                "id":capturar_pokemon.id, 
                "nick_name":capturar_pokemon.nick_name, 
                "is_party_member":capturar_pokemon.is_party_member, 
                "specie": capturar_pokemon.specie_id,
                "mensaje": "Pokemon, Capturado"
                }
            )


#VISTA MOSTRAR LOS POKEMONES CAPTURADOS Y ESTE EN LA FIESTA
class MostrarPokemonCapturados(ListAPIView):
    serializer_class = PokemonCapturadoSerializer
    pagination_class = PagSerializer

    def get_queryset(self):
        return AlmacenPokemonCapturado.objects.filter(is_party_member= True)
    

class MostrarPokemonCapturadosPorLink(ListAPIView):
    serializer_class = PokemonCapturadoPorLinkSerializer
    pagination_class = PagSerializer

    def get_queryset(self):
        return AlmacenPokemonCapturado.objects.filter(is_party_member= True)
    

#VISTA DE REGIONES
class ListarRegiones(ListAPIView):

    serializer_class = RegionSerializer
    #queryset = Region.objects.regiones()

    def  get_queryset(self):
        return Region.objects.all()
    

#VISTA DE REGIONES CON DETALLADAS => 
class ListarLocationRegion(ListAPIView):
    serializer_class = RegionLocationSerializer

    def get_queryset(self):
        region_id = self.kwargs['pk'] 

        return Region.objects.filter(id = region_id)



#VISTA DE LOCATIONS DETALLADAS
class DetailLocations(ListAPIView):
    serializer_class = DetallarLocationsSerializer

    def get_queryset(self):
        
        location_id = self.kwargs['pk']

        return Location.objects.filter(id = location_id)


#VISTA DE LOCATIONS DETALLADAS
class DetailArea(ListAPIView):
    serializer_class = DetailAreaSerializer

    def get_queryset(self):
        
        area_id = self.kwargs['pk']

        return Area.objects.filter(id = area_id)
        #return  Area.objects.all()

#class DetallarArea(ListCreateAPIView):
 #   serializer_class = DetailAreaSerializer


#VISTA DE UDPATE ALMACEN DE POKEMON
class AlmacenPokemonUpdateView(UpdateAPIView): 
#class AlmacenPokemonUpdateView(RetrieveUpdateAPIView): 

    serializer_class = UpdateAlmacenPokemon
    queryset = AlmacenPokemonCapturado.objects.all()

   # def get_queryset(self):
    #    x = AlmacenPokemonCapturado.objects.get(id = self.kwargs['pk'])
     #   return x

    def update(self, request, *args, **kwargs):
        
        #partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = UpdateAlmacenPokemon(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        x = AlmacenPokemonCapturado.objects.filter(id = instance.id).values()
        return Response( x)
            
    
#VISTA PARA ELIMINAR
class DeletePokemon(DestroyAPIView):
#class DeletePokemon(RetrieveDestroyAPIView):

    serializer_class = RegionSerializer
    queryset = Region.objects.all()
