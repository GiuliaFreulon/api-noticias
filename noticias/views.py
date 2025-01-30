from django.views import View
from django.http import JsonResponse
import uuid
import json
from datetime import datetime

banco = {}

class NoticiaView(View):
    def get(self, request):
        # Lista todas as notícias
        return JsonResponse(list(banco.values()), safe=False)

    def post(self, request):
        # Adiciona uma nova notícia
        try:
            data = json.loads(request.body)
            identificador = uuid.uuid4().hex
            data_criacao = str(datetime.now())
            banco[identificador] = {
                'id': identificador,
                'titulo': data['titulo'],
                'conteudo': data['conteudo'],
                'autor': data['autor'],
                'data_publicacao': data_criacao
            }
            return JsonResponse(banco[identificador], status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

class NoticiaDetailView(View):
    def get(self, request, id):
        # Obtém uma notícia específica por ID
        if id in banco:
            return JsonResponse(banco[id])
        return JsonResponse({'error': 'Notícia não encontrada'}, status=404)

    def put(self, request, id):
        # Atualiza uma notícia existente por ID
        if id in banco:
            try:
                data = json.loads(request.body)
                banco[id].update({
                    'titulo': data['titulo'],
                    'conteudo': data['conteudo'],
                    'autor': data['autor'],
                    'data_publicacao': banco[id]['data_publicacao']  # Mantém a data de publicação original
                })
                return JsonResponse(banco[id])
            except json.JSONDecodeError:
                return JsonResponse({'error': 'JSON inválido'}, status=400)
        return JsonResponse({'error': 'Notícia não encontrada'}, status=404)

    def patch(self, request, id):
        # Atualiza parcialmente uma notícia existente por ID
        return self.put(request, id)  # Reutiliza o método put para patch

    def delete(self, request, id):
        # Remove uma notícia existente por ID
        if id in banco:
            del banco[id]
            return JsonResponse({'message': 'Notícia removida com sucesso'}, status=200)
        return JsonResponse({'error': 'Notícia não encontrada'}, status=404)
