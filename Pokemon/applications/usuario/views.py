from django.shortcuts import render
from django.utils import timezone

#rest_frameword
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from rest_framework.views import APIView
from rest_framework.generics import(
    ListAPIView, CreateAPIView
)
#serializers
from .serializers import AutenticarUserSerializers
from .functions import AsignarTokenUsuario

class AutenticacionUsuarioToken(APIView):

    serializer_class = AutenticarUserSerializers
    
    def post (self, request):
        serializer = self.serializer_class( data = request.data)
        
        if serializer.is_valid(raise_exception=True):
            
            respuesta = AsignarTokenUsuario(request.data)
            
            return Response(
                {
                    "Token": respuesta
                }
            )

        ''' else:
            return Response(
                    {
                        "Mensaje": "Serializer Incorrecto"
                    }
                ) '''
        
      
        