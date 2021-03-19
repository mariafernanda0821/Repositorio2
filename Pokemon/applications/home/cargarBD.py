import json
#from rest_framework.response import Response
from .models import (
    Region, Area, Location,Pokemon, Habilidades, Moves,
    Sprites, Types, Stats,
    )

#from django.models import area_pokemon
def Cargar_Region(request):
    data = False 
    Region_data = json.load(open("regions.json",'r'))
    for region in Region_data["data"]:
        if Region.objects.filter(region_name = region["name"]).exists():
                continue
        else:
            r = Region.objects.create(region_name = region["name"])
            r.save()
            print(r)
        data = True
        print(data)
    return data


def Cargar_Localidad(request):
    data = False 

    Location_data = json.load(open("locations.json",'r'))

    for location in Location_data["data"]:
        if  Location.objects.filter(location_name = location["name"]).exists():
            continue
        else:
            region_id = Region.objects.filter(region_name =location["region"]).values("id")
            l = Location.objects.create(location_name = location["name"], region_id = region_id)
            l.save()
            print(l) 
    data = True
    print(data)

    return data


def Cargar_Pokemon(request):
    data = False 
    Pokemon_data = json.load(open("pokemons.json",'r')) 

    for pokemon in Pokemon_data["data"]:
        if  Pokemon.objects.filter(pokemon_name = pokemon["name"]).exists():
            continue
        else:

            #for sprites in pokemon["sprites"]:
                
            sp = Sprites.objects.create(
                    back_default = pokemon["sprites"]["back_default"],
                    back_female = pokemon["sprites"]["back_female"],
                    back_shiny = pokemon["sprites"]["back_shiny"],
                    back_shiny_female = pokemon["sprites"]["back_shiny_female"],
                    front_default = pokemon["sprites"]["front_default"],
                    front_female = pokemon["sprites"]["front_female"],
                    front_shiny = pokemon["sprites"]["front_shiny"],
                    front_shiny_female = pokemon["sprites"]["front_shiny_female"],
            )
            sp.save()
            print("sprites===>", sp.id)
            print("=============",sp)

                #sprite_id = Types.objects.get(types_name =movimiento)
            #p.sprites.add(sp.id)

            stats = pokemon["stats"]
               
            st = Stats.objects.create(
                    stats_SPEED = stats[0]["value"],
                    stats_SPECIAL_DEFENSE = stats[1]["value"],
                    stats_SPECIAL_ATTACK = stats[2]["value"],
                    stats_DEFENSE = stats[3]["value"],
                    stats_ATTACK = stats[4]["value"], 
                    stats_HP = stats[5]["value"], 
            )
            st.save()
            print("Stats===>", st)
            print("=============")
            
            #p.stats.add(st.id)

            p = Pokemon.objects.create(
                pokemon_name = pokemon["name"],
                pokemon_capture_rate = pokemon["capture_rate"],
                pokemon_color = pokemon["color"],
                pokemon_flavor_text = pokemon["flavor_text"],
                pokemon_height = pokemon["height"],
                pokemon_weight = pokemon["weight"],
                sprites_id = sp.id, 
                stats_id = st.id

            )

                         
            for habilidad in pokemon["abilities"]:
                if Habilidades.objects.filter(habilidad_name = habilidad).exists():
                    continue
                else:
                    ha = Habilidades.objects.create(habilidad_name = habilidad)
                    ha.save
                    print("Habilidad===>", ha)
                    print("=============")
                
                habilidad_id = Habilidades.objects.get(habilidad_name =habilidad)
                p.habilidad.add(habilidad_id)
            

            for movimiento in pokemon["moves"]:
                if Moves.objects.filter(moves_name = movimiento).exists():
                    continue
                else:
                    mo= Moves.objects.create(moves_name = movimiento)
                    mo.save
                    print("movimiento===>", mo)
                    print("=============")
                
                movimiento_id = moves.objects.get(moves_name =movimiento)  
                p.move.add(movimiento_id)
            
            for tipo in pokemon["types"]:
                if Types.objects.filter(types_name = tipo).exists():
                    continue
                else:
                    t =Types.objects.create(types_name = tipo)
                    t.save
                    print("Typos===>", t)
                    print("=============")

                
                type_id = Types.objects.get(types_name =movimiento)
                p.move.add(type_id) 


        p.save()
    data = True
    print(data)
        
    return data

def Cargar_Area(request):
    data = False 
    Areas_data = json.load(open("areas.json",'r')) 
    
    for area in Areas_data["data"]:

        if Area.objects.filter(area_name = area["name"]).exists():
            continue
        else:
            location_id = Location.objects.filter(location_name = area["location"]).values("id")  
            a = Area.objects.create(area_name = area["name"], location_id = location_id)
            print(a)

            for x in area["pokemons"]:
                pokemon_id = Pokemon.objects.get(pokemon_name = x.title())
                print("======>", pokemon_id)
                print("vvalor de x ======>", x)
                a.pokemon.add(pokemon_id)
                
        print(a)
        a.save()
        
    data = True
    print(data)
    return (data)
            


