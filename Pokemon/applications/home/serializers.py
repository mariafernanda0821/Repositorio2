from rest_framework import serializers, pagination
from .models import *
from django.db.models import Count


class PagSerializer(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 100


class HabilidadSerializer(serializers.ModelSerializer):
   
    #habilidads = serializers.SerializerMethodField() 
    
    class Meta:
        model = Habilidades
       # exclude = ['habilidad_name', 'id']
        fields = (
            "habilidad_name",
            #"habilidads",
        )

    # def get_habilidads(self, obj):
    #     print("====>", obj.id)
    #     print("====>", obj.habilidad_name)

    #     #a = Habilidades.objects.filter(id = obj.id).values("habilidad_name")
    #     return str(obj.id) + " " +  obj.habilidad_name

class TypesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Types
        fields = (
            "types_name",
        )


class MoveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Moves
        fields = (
            "moves_name",
        )


class SpritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprites
        fields = (
            "back_default",
            "back_female",
            "back_shiny",
            "back_shiny_female",
            "front_default",
            "front_female",
            "front_shiny",
            "front_shiny_female",   
        )


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ("__all__")


class PokemonDescripcionSerializer(serializers.ModelSerializer):
    
    #habilidad = HabilidadSerializer(many = True) 
    habilidad = serializers.SerializerMethodField()
    move = serializers.SerializerMethodField()
    types =serializers.SerializerMethodField()
    sprites = SpritesSerializer()
    stats = StatsSerializer()
    #habilidads = serializers.SerializerMethodField() 

    class Meta:
        model = Pokemon
        fields = (
            'id',
            "pokemon_name" ,
            "pokemon_capture_rate" , 
            "pokemon_color" ,
            "pokemon_flavor_text" ,
            "pokemon_height" ,
            "pokemon_weight" ,
            "habilidad" ,
            "move" ,
            "types",
            "sprites",
            "stats",
        )

    def get_habilidad(self, obj):
        #print(===>, obj.habilidad)
        hab = []
        query = Habilidades.objects.filter(pokemon= obj.id).values("habilidad_name")
        
        for x in query:
            #print(x["habilidad_name"])
            hab.append(x['habilidad_name'])
        #print("==>", hab)
        return hab
    
    def get_move(self, obj):
        #print(===>, obj.habilidad)
        move = []
        query = Moves.objects.filter(pokemon= obj.id).values("moves_name")
        
        for x in query:
            #print(x["habilidad_name"])
            move.append(x['moves_name'])
        #print("==>", hab)
        return move
 
    def get_types(self, obj):
        #print(===>, obj.habilidad)
        types = []
        query = Types.objects.filter(pokemon= obj.id).values("types_name")
        
        for x in query:
            #print(x["habilidad_name"])
            types.append(x['types_name'])
        #print("==>", hab)
        return types

class CapturarPokemomSerializer(serializers.Serializer):

    #pass 
    specie = serializers.IntegerField()
    nick_name = serializers.CharField()
    is_party_member = serializers.BooleanField()


class PokemonCapturadoSerializer(serializers.ModelSerializer):

    specie = serializers.SerializerMethodField()
   
    class Meta:
        model = AlmacenPokemonCapturado
        fields = (
            'id',
            'nick_name',
            'is_party_member',
            'specie',
        )   

    def get_specie(self, obj): #obj nos indica el id de que se esta interando
        
        query = Pokemon.objects.filter(id = obj.specie_id)

        pokemones = PokemonDescripcionSerializer(query, many=True).data

        return pokemones


#seializer de link
class PokemonCapturadoPorLinkSerializer(serializers.HyperlinkedModelSerializer):

   # specie = serializers.SerializerMethodField()
   
    class Meta:
        model = AlmacenPokemonCapturado
        fields = (
            'id',
            'nick_name',
            'is_party_member',
            'specie',
        )   

        extra_kwargs = { #los atributos que necesito para que sea un link
                'specie' : {
                    'view_name': 'home_app:pokemon_descripcion',
                    'lookup_field': 'pk'
                }
            }


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region 
        fields = (
            'id',
            'region_name'
        )


#serializer de locations
class LocationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'id',
            'location_name'
        )


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = (
            'id',
            'area_name'
        )


#muestra todo la informacion de region 
class RegionLocationSerializer(serializers.ModelSerializer):
    
    location = serializers.SerializerMethodField()
   
    class Meta:
        model = Region
        fields = (
            'id',
            'location',
            'region_name'
        )

    def get_location(self, obj):
        query = Location.objects.filter(region_id = obj.id)
        locaciones = LocationsSerializer(query, many=True).data
        return locaciones


#muestra todo la informacion de locations
class DetallarLocationsSerializer(serializers.ModelSerializer):

    area = serializers.SerializerMethodField()
    class Meta:
        model = Location
        fields = (
            'id',
            'area',
            'location_name',
            'region'
        )

    def get_area(self, obj):

        query = Area.objects.filter(location_id= obj.id)
        
        areas = AreaSerializer(query, many=True).data
        #print("====>", areas)
        return areas


class DetailAreaSerializer(serializers.ModelSerializer):

    #pokemons = serializers.SerializerMethodField()
    pokemon = PokemonDescripcionSerializer(many = True)
    pokemon_count = serializers.SerializerMethodField() 

    class Meta:
        model = Area
        fields = (
            'id',
            'pokemon_count',
            'pokemon',
            'area_name',
            'location'
        )

    def get_pokemon_count(self, obj):
        query = Area.objects.filter(id = obj.id).values("pokemon").count()
        #contar = ContarPokemons(query)
        #print(query)
        return query



class UpdateAlmacenPokemon(serializers.Serializer):

    nick_name = serializers.CharField()

    def update(self, instance, validated_data):

        instance.nick_name = validated_data["nick_name"]
        instance.save()
        return instance