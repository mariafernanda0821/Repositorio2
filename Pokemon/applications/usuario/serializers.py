from rest_framework import serializers

#models
from django.contrib.auth.models import User

class AutenticarUserSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

