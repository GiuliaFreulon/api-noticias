from rest_framework import serializers

class NoticiaSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    titulo = serializers.CharField(max_length=255)
    conteudo = serializers.CharField()
    autor = serializers.CharField(max_length=255)