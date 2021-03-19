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