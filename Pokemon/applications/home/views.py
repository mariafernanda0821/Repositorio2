from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny
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


#VISTA DE DESCRIPCION DE CADA POKEMON => Pokemon specie detail
class DescripcionPokemon(ListAPIView):

    serializer_class = PokemonDescripcionSerializer
    permission_classes = [AllowAny, ]
    http_method_names = ['get']

    def get_queryset(self):

        pokemon_id = self.kwargs['pk'] 

        return Pokemon.objects.detalles_pokemon(pokemon_id)

    def dispatch(self, request, *args, **kwargs):
        """
        `.dispatch()` is pretty much the same as Django's regular dispatch,
        but with extra hooks for startup, finalize, and exception handling.
        """
        self.args = args
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?

        try:
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            response = handler(request, *args, **kwargs)

        except Exception as exc:
            response = self.handle_exception(exc)

        self.response = self.finalize_response(request, response, *args, **kwargs)
        return self.response


#VISTA DE CAPTURAR UN POKEMON =>  Pokemon catch
class CapturarPokemon(CreateAPIView):

    serializer_class = CapturarPokemomSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['post', ]


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


#VISTA MOSTRAR LOS POKEMONES CAPTURADOS Y incluida lo de la FIESTA (usuario) => Pokemon Storage
class MostrarPokemonCapturados(ListAPIView):
    serializer_class = PokemonCapturadoSerializer
    pagination_class = PagSerializer
    #authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    def get_queryset(self):
        return AlmacenPokemonCapturado.objects.all()
    

class MostrarPokemonCapturadosPorLink(ListAPIView):
    serializer_class = PokemonCapturadoPorLinkSerializer
    pagination_class = PagSerializer

    def get_queryset(self):
        return AlmacenPokemonCapturado.objects.filter(is_party_member= True)
    

#VISTA DE UDPATE ALMACEN DE POKEMON => Pokemon rename
class AlmacenPokemonUpdateView(UpdateAPIView): 
#class AlmacenPokemonUpdateView(RetrieveUpdateAPIView): 

    serializer_class = UpdateAlmacenPokemon
    queryset = AlmacenPokemonCapturado.objects.all()
    #authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated, ]

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



#VISTA DE REGIONES => Regions list
class DetailRegiones(ListAPIView):

    serializer_class = RegionSerializer
    permission_classes = [AllowAny, ] 
    #queryset = Region.objects.regiones()

    def  get_queryset(self):
        return Region.objects.all()
    

#VISTA DE REGIONES CON DETALLADAS => Regions detail
class DetailRegionLocation(ListAPIView):
    serializer_class = RegionLocationSerializer
    permission_classes = [AllowAny, ] 

    def get_queryset(self):
        region_id = self.kwargs['pk'] 

        return Region.objects.filter(id = region_id)



#VISTA DE LOCATIONS DETALLADAS => Location detail
class DetailLocations(ListAPIView):
    serializer_class = DetallarLocationsSerializer
    permission_classes = [AllowAny, ] 

    def get_queryset(self):
        
        location_id = self.kwargs['pk']

        return Location.objects.filter(id = location_id)


#VISTA DE LOCATIONS DETALLADAS => Area detail
class DetailArea(ListAPIView):
    serializer_class = DetailAreaSerializer
    permission_classes = [AllowAny, ] 

    def get_queryset(self):
        
        area_id = self.kwargs['pk']

        return Area.objects.filter(id = area_id)
        #return  Area.objects.all()

