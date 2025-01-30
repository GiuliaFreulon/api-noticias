from django.views import View
from django.http import JsonResponse
import json
from .memory_db import BancoDeNoticias
from .serializers import NoticiaSerializer

banco_de_noticias = BancoDeNoticias()

class NoticiaView(View):
    def get(self, request):
        try:
            noticias = banco_de_noticias.listar_todas_noticias()
            return JsonResponse(noticias, safe=False, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = NoticiaSerializer(data=data)
            if serializer.is_valid():
                noticia = banco_de_noticias.adicionar_noticia(serializer.validated_data)
                return JsonResponse(noticia, status=201)
            return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class NoticiaDetailView(View):
    def get(self, request, id):
        try:
            noticia = banco_de_noticias.obter_noticia(id)
            if 'error' in noticia:
                return JsonResponse(noticia, status=404)
            return JsonResponse(noticia, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def put(self, request, id):
        try:
            data = json.loads(request.body)
            serializer = NoticiaSerializer(data=data)
            if serializer.is_valid():
                noticia = banco_de_noticias.editar_noticia(id, serializer.validated_data)
                if 'error' in noticia:
                    return JsonResponse(noticia, status=404)
                return JsonResponse(noticia, status=200)
            return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def patch(self, request, id):
        try:
            data = json.loads(request.body)
            serializer = NoticiaSerializer(data=data, partial=True)
            if serializer.is_valid():
                noticia = banco_de_noticias.editar_noticia(id, serializer.validated_data)
                if 'error' in noticia:
                    return JsonResponse(noticia, status=404)
                return JsonResponse(noticia, status=200)
            return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def delete(self, request, id):
        try:
            resultado = banco_de_noticias.remover_noticia(id)
            if 'error' in resultado:
                return JsonResponse(resultado, status=404)
            return JsonResponse(resultado, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
