from django.contrib import admin
from .models import (
    Region, Area, Location,Pokemon, Habilidades, Moves,
    Sprites, Types, Stats,
    )
admin.site.register(Region)
admin.site.register(Area)
admin.site.register(Location)
admin.site.register(Pokemon)
admin.site.register(Habilidades)
admin.site.register(Moves)
admin.site.register(Sprites)
admin.site.register(Types)
admin.site.register(Stats)



# Register your models here.
