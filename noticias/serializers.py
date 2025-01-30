from rest_framework import serializers

class NoticiaSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    titulo = serializers.CharField(max_length=255)
    conteudo = serializers.CharField()
    autor = serializers.CharField(max_length=255)

    def validate_titulo(self, value):
        if not value:
            raise serializers.ValidationError("O título é obrigatório.")
        return value

    def validate_conteudo(self, value):
        if not value:
            raise serializers.ValidationError("O conteúdo é obrigatório.")
        return value

    def validate_autor(self, value):
        if not value:
            raise serializers.ValidationError("O autor é obrigatório.")
        return value