from django.db import models
from django.contrib.auth.models import User 
#manager
from .managers import (
    PokemonManager, AlmacenPokemonManager, RegionManager, AreaManager, LocationManager
)

class Region(models.Model):

    region_name = models.CharField(unique = True, max_length=30)
    
    objects = RegionManager()

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

    def __str__(self):
        return str(self.id) + " "+ self.region_name 


class Location(models.Model):
    
    location_name =  models.CharField( unique = True,  max_length=80)
    region = models.ForeignKey(Region, on_delete = models.CASCADE)  

    objects = LocationManager()

    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"

        def __str__(self):
            return str(self.id) + " "+ self.location_name


class Habilidades(models.Model):
   
    habilidad_name = models.CharField( unique = True, max_length=80)
    #pokemon = models.ManyToManyField(Pokemon)
   

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

        def __str__(self):
            return str(self.id) + " "+ self.habilidad_name


class Moves(models.Model):
    
    moves_name= models.CharField( unique = True, max_length=80)
   # pokemon = models.ManyToManyField(Pokemon)

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"

        def __str__(self):
            return str(self.id) + " "+ self.moves_name
    

class Sprites(models.Model):
    
    back_default = models.CharField(null = True, blank = True, max_length=200, default= "null")
    back_female = models.CharField(null = True, blank = True, max_length=200, default= "null")
    back_shiny = models.CharField(null = True, blank = True, max_length=200, default= "null")
    back_shiny_female = models.CharField(null = True, blank = True, max_length=200, default= "null")
    front_default = models.CharField(null = True, blank = True, max_length=200, default= "null")
    front_female = models.CharField(null = True, blank = True, max_length=200, default= "null")
    front_shiny = models.CharField(null = True, blank = True, max_length=200, default= "null")
    front_shiny_female = models.CharField(null = True, blank = True, max_length=200,default= "null")
    
    class Meta:
        verbose_name = "Sprite"
        verbose_name_plural = "Sprites"

        def __str__(self):
            return str(self.id)


class Types(models.Model):
    #id = models.AutoField(primary_key = False)
    types_name = models.CharField(unique = True, max_length=80)

    class Meta:
        verbose_name = "Tipos"
        verbose_name_plural = "Tipos de POkemon"

        def __str__(self):
            return str(self.id) + " "+ self.types_name


class Stats(models.Model):
    stats_SPEED = models.IntegerField()
    stats_SPECIAL_DEFENSE = models.IntegerField()
    stats_SPECIAL_ATTACK = models.IntegerField()
    stats_DEFENSE = models.IntegerField()
    stats_ATTACK = models.IntegerField() 
    stats_HP = models.IntegerField() 
   
    class Meta:
        verbose_name = "Stats"
        verbose_name_plural = "Stats de Pokemon"

        def __str__(self):
            return str(self.id) 


class Pokemon(models.Model):
    
    pokemon_name = models.CharField( unique= True, max_length=80)
    pokemon_capture_rate = models.CharField( null= True, blank = True, max_length=80)
    pokemon_color = models.CharField(null = True, blank = True, max_length=80)
    pokemon_flavor_text = models.TextField(blank = True)
    pokemon_height = models.IntegerField( default= 0)
    pokemon_weight = models.IntegerField(default= 0)
    habilidad = models.ManyToManyField(Habilidades) 
    move = models.ManyToManyField(Moves) 
    types = models.ManyToManyField(Types)
    sprites = models.OneToOneField(Sprites, on_delete = models.CASCADE)
    stats = models.OneToOneField(Stats, on_delete = models.CASCADE)
    objects = PokemonManager()

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemones"

        def __str__(self):
            return str(self.id) + " "+ self.pokemon_name


class Area(models.Model):
    area_name= models.CharField( unique = True, max_length=80)
    location = models.ForeignKey( Location , on_delete = models.CASCADE)
    pokemon = models.ManyToManyField(Pokemon)
    
    objects = AreaManager()

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

        def __str__(self):
            return str(self.id) + " "+ self.area_name


class AlmacenPokemon(models.Model):

    pokemon = models.ForeignKey(Pokemon , on_delete = models.CASCADE) 
    #id_usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    nick_name = models.CharField(max_length=20)
    is_party_member = models.BooleanField(default= False)

class AlmacenPokemonCapturado(models.Model):
    
    specie = models.ForeignKey(Pokemon, on_delete = models.CASCADE) 
    nick_name = models.CharField(max_length=20)
    is_party_member = models.BooleanField(default= False)

    objects = AlmacenPokemonManager()

    class Meta:
        verbose_name = "Almacen de Pokemon"
        verbose_name_plural = "Almacen de Pokemon Capturados"