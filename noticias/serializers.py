from rest_framework import serializers

class NoticiaSerializer(serializers.Serializer):
    titulo = serializers.CharField(max_length=255)
    conteudo = serializers.CharField()
    autor = serializers.CharField(max_length=255)

    def validate_titulo(self, value):
        if not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError("O campo 'titulo' deve ser uma string não vazia.")
        return value

    def validate_conteudo(self, value):
        if not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError("O campo 'conteudo' deve ser uma string não vazia.")
        return value

    def validate_autor(self, value):
        if not isinstance(value, str) or not value.strip():
            raise serializers.ValidationError("O campo 'autor' deve ser uma string não vazia.")
        return value
