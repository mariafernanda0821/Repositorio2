<<<<<<< HEAD
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from django.utils import timezone
from django.shortcuts import get_object_or_404

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


# class PokemonViewSets(viewsets.ViewSet):
#     #queryset = Pokemon.objects.all()
#     #serializer_class = PokemonDescripcionSerializer

#     def retrieve(self, request, pk=None):
#         queryset = get_object_or_404(Pokemon.objects.detalles_pokemon(pk))
#         #queryset = get_object_or_404(Pokemon.objects.all(), pk=pk)
#         serializer = PokemonDescripcionSerializer(queryset)
#         return Response(serializer.data)



class PokemonCapturadoViewSets(viewsets.ViewSet):
   
    #serializer_class = PokemonCapturadoSerializer
    #queryset = AlmacenPokemonCapturado.objects.all() 

    def list(self, request):

        queryset = AlmacenPokemonCapturado.objects.all() 

        serializer = PokemonCapturadoSerializer(queryset, many=True)

        return Response (serializer.data)


    def create(self, request):
        
        serializer = CapturarPokemomSerializer(data= request.data)

        serializer.is_valid(raise_exception=True) 

        pokemon = Pokemon.objects.get(id=serializer.validated_data["specie"])
        capturar_pokemon = AlmacenPokemonCapturado.objects.capturar_pokemon(serializer, pokemon)
            #capturar_pokemon.save()
        x =AlmacenPokemonCapturado.objects.filter(id=capturar_pokemon.id).values()
        #print("=====>", x)
        return Response ( x
                    # {
                    # "id":capturar_pokemon.id, 
                    # "nick_name":capturar_pokemon.nick_name, 
                    # "is_party_member":capturar_pokemon.is_party_member, 
                    # "specie": capturar_pokemon.specie_id,
                    # "mensaje": "Pokemon, Capturado"
                    # }
                )


    def update(self, request, pk=None):
        try:
            instance = AlmacenPokemonCapturado.objects.get(specie=pk)
        except AlmacenPokemonCapturado.DoesNotExist:
            return Response("Ningun usuario tiene capturado a esa especie.")
        
        serializer = UpdateAlmacenPokemon(pk,data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.nick_name = serializer.validated_data["nick_name"]
        instance.save()
        x = AlmacenPokemonCapturado.objects.filter(id = instance.id).values()
        
        return Response( x)


    def destroy(self, request, pk=None):
        try:
            instance = AlmacenPokemonCapturado.objects.get(specie=pk)
        except AlmacenPokemonCapturado.DoesNotExist:
            return Response("No se puede eliminar esa especie de pokemon, por que no esta capturado.")
        #instance = AlmacenPokemonCapturado.objects.filter(specie=pk).first().delete()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class PokemonOwnViewSets(viewsets.ViewSet):
#     serializer_class = PokemonCapturadoSerializer
#     pagination_class = PagSerializer
#     #authentication_classes = (TokenAuthentication, )
#     permission_classes = [IsAuthenticated, ]
#     http_method_names = ['get', ]

#     def get_queryset(self):
#         return AlmacenPokemonCapturado.objects.all() 


class PokemonOwnViewSets(viewsets.ViewSet):
   # @action(detail=True, methods=['post'])
    pass


class RegionViewSet(viewsets.ViewSet):

    def list(self, request):
        #print("entre a list =====>", request.data)
        queryset = Region.objects.all()
       # serializer_class = RegionSerializer
        serializer = RegionSerializer(queryset, many = True)
        #print(serializer)
        return Response(
            serializer.data )
       
    def retrieve(self, request, pk=None):
        queryset = Region.objects.filter(id=pk)
        #print(queryset, "================")
        serializer = RegionLocationSerializer(queryset, many = True)  
        return Response( serializer.data)
   

class LocationViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Location.objects.filter(id = pk)
        serializer = DetallarLocationsSerializer(queryset, many=True)
        return Response(serializer.data)
=======
back_default= "http=//raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
back_female= null,
back_shiny= "http=//raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/1.png",
back_shiny_female= null,
front_default= "http=//raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
front_female= null,
front_shiny= "http=//raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png",
front_shiny_female= null


a= [
                {
                    "name": "speed",
                    "value": 45
                },
                {
                    "name": "special-defense",
                    "value": 65
                },
                {
                    "name": "special-attack",
                    "value": 65
                },
                {
                    "name": "defense",
                    "value": 49
                },
                {
                    "name": "attack",
                    "value": 49
                },
                {
                    "name": "hp",
                    "value": 45
                }
            ],


            #VISTA DE UDPATE ALMACEN DE POKEMON
class HabilidadUpdateView(RetrieveUpdateAPIView):
    serializer_class = HabilidadSerializer
    queryset = Habilidades.objects.all()

#VISTA DE UDPATE ALMACEN DE POKEMON
class Habilidad2UpdateView(UpdateAPIView):
    serializer_class = HabilidadSerializer
    queryset = Habilidades.objects.all()


{
"specie":100,
"nick_name":"fernanda",
"is_party_member":true
}
>>>>>>> segunda
