from rest_framework.authtoken.models import Token 
from django.contrib.auth import authenticate
#from django.contrib.auth.models import User

def AsignarTokenUsuario(data):
    user = authenticate(username = data["username"] , password = data["password"])
    if user is not None:
        token ,created = Token.objects.get_or_create(user = user)
        #print(token.key)
        return (token.key)
    else:
        #print("usuario No valido")
        return ("Usuario no existe. ")
            # No backend authenticated the credentials
