import uuid
import json
from datetime import datetime
from django.http import JsonResponse

banco = {}

def adicionar_noticia(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            identificador = uuid.uuid4().hex
            data_criacao = str(datetime.now())
            banco[identificador] = {
                'id': identificador,
                'titulo': data['titulo'],
                'conteudo': data['conteudo'],
                'autor': data['autor'],
                'data_criacao': data_criacao
            }
            return JsonResponse(banco[identificador], status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
    else:
        return JsonResponse({'error': 'Método não permitido, use POST para adicionar notícias'}, status=405)

def obter_noticia(request, id):
    if id in banco:
        return JsonResponse(banco[id])
    return JsonResponse({'error': 'Notícia não encontrada'}, status=404)

def listar_todas_noticias(request):
    return JsonResponse(banco, safe=False)

def editar_noticia(request, id):
    if request.method == 'PUT' or request.method == 'PATCH':
        if id in banco:
            data = request.data
            banco[id].update({
                'titulo': data['titulo'],
                'conteudo': data['conteudo'],
                'autor': data['autor'],
                'data_criacao': banco[id]['data_criacao']
            })
            return JsonResponse(banco[id])
        return JsonResponse({'error': 'Notícia não encontrada'}, status=404)

def remover_noticia(request, id):
    if id in banco:
        del banco[id]
        return JsonResponse({'message': 'Notícia removida com sucesso'}, status=204)
    return JsonResponse({'error': 'Notícia não encontrada'}, status=404)