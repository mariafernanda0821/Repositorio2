from django.db import models
from django.db.models import Count


class PokemonManager(models.Manager):

    def detalles_pokemon(self, pokemon_id):
    
        return self.filter(id= pokemon_id)


class AlmacenPokemonManager(models.Manager):
    
    def contar_usuario(self, nick_name):

        contar = self.filter(nick_name = nick_name).count()
        
        return contar

    def capturar_pokemon(self,serializer, pokemon):
       # print("pokemon_id ====>", pokemon_id)
       # print("serializer ====>", serializer)
       # print(" data ====>", serializer.data)


        return self.create(
                specie = pokemon, 
                nick_name = serializer.validated_data["nick_name"],
                is_party_member = serializer.validated_data["is_party_member"]
            )


    def  pokemones_capturado(self, specie_id):
        
        return  self.filter(
            is_party_member = True
        )


class RegionManager(models.Manager):
    def regiones(self):
        return self.all()


class LocationManager(models.Manager):
    def buscar_region(self, region_id):
        return self.filter(region_id = region_id)


class AreaManager(models.Manager):
    pass

