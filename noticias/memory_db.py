import uuid
from datetime import datetime

class BancoDeNoticias:
    def __init__(self):
        self.banco = {}

    def listar_todas_noticias(self):
        return list(self.banco.values())

    def adicionar_noticia(self, data):
        identificador = uuid.uuid4().hex
        data_criacao = str(datetime.now())
        self.banco[identificador] = {
            'id': identificador,
            'titulo': data['titulo'],
            'conteudo': data['conteudo'],
            'autor': data['autor'],
            'data_publicacao': data_criacao
        }
        return self.banco[identificador]

    def obter_noticia(self, id):
        return self.banco.get(id, {'error': 'Notícia não encontrada'})

    def editar_noticia(self, id, data):
        if id in self.banco:
            self.banco[id].update(data)
            return self.banco[id]
        return {'error': 'Notícia não encontrada'}

    def remover_noticia(self, id):
        if id in self.banco:
            del self.banco[id]
            return {'message': 'Notícia removida com sucesso'}
        return {'error': 'Notícia não encontrada'}