from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serialzer a name field fro testing our ApiView"""
    name = serializers.CharField(max_length=10)
