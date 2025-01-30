import os
import django
from django.test import TestCase, Client
from django.urls import reverse
import json

os.environ['DJANGO_SETTINGS_MODULE'] = 'noticias_api.settings'

django.setup()

class NoticiaAPITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.noticia_url = reverse('noticia-list-create')
        self.noticia_detail_url = lambda id: reverse('noticia-detail', args=[id])
        self.valid_payload = {
            'titulo': 'Teste de Titulo',
            'conteudo': 'Conteudo de Teste',
            'autor': 'Autor de Teste'
        }
        self.invalid_payload = {
            'titulo': '',
            'conteudo': '',
            'autor': ''
        }

    def test_criar_noticia_valida(self):
        response = self.client.post(
            self.noticia_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())
        self.assertIn('data_publicacao', response.json())

    def test_criar_noticia_invalida(self):
        response = self.client.post(
            self.noticia_url,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_listar_noticias(self):
        self.client.post(
            self.noticia_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        response = self.client.get(self.noticia_url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_obter_noticia_existente(self):
        post_response = self.client.post(
            self.noticia_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        noticia_id = post_response.json().get('id')
        get_response = self.client.get(self.noticia_detail_url(noticia_id))
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.json().get('id'), noticia_id)

    def test_obter_noticia_inexistente(self):
        response = self.client.get(self.noticia_detail_url('nonexistent-id'))
        self.assertEqual(response.status_code, 404)

    def test_editar_noticia_existente(self):
        post_response = self.client.post(
            self.noticia_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        noticia_id = post_response.json().get('id')
        updated_payload = {
            'titulo': 'Titulo Atualizado',
            'conteudo': 'Conteudo Atualizado',
            'autor': 'Autor Atualizado'
        }
        put_response = self.client.put(
            self.noticia_detail_url(noticia_id),
            data=json.dumps(updated_payload),
            content_type='application/json'
        )
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(put_response.json().get('titulo'), 'Titulo Atualizado')

    def test_editar_noticia_inexistente(self):
        noticia_id_inexistente = 'nonexistent-id'
        updated_payload = {
            'titulo': 'Titulo Atualizado',
            'conteudo': 'Conteudo Atualizado',
            'autor': 'Autor Atualizado'
        }
        put_response = self.client.put(
            self.noticia_detail_url(noticia_id_inexistente),
            data=json.dumps(updated_payload),
            content_type='application/json'
        )
        self.assertEqual(put_response.status_code, 404)
        self.assertIn('error', put_response.json())

    def test_editar_noticia_com_dados_invalidos(self):
        post_response = self.client.post(
            self.noticia_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        noticia_id = post_response.json().get('id')
        updated_payload_invalido = {
            'titulo': '',
            'conteudo': '',
            'autor': ''
        }
        put_response = self.client.put(
            self.noticia_detail_url(noticia_id),
            data=json.dumps(updated_payload_invalido),
            content_type='application/json'
        )
        self.assertEqual(put_response.status_code, 400)

    def test_remover_noticia_existente(self):
        post_response = self.client.post(
            self.noticia_url,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        noticia_id = post_response.json().get('id')
        delete_response = self.client.delete(self.noticia_detail_url(noticia_id))
        self.assertEqual(delete_response.status_code, 200)

    def test_remover_noticia_inexistente(self):
        delete_response = self.client.delete(self.noticia_detail_url('nonexistent-id'))
        self.assertEqual(delete_response.status_code, 404)

    def test_criar_noticia_com_campos_extras(self):
        payload_com_extras = {
            'titulo': 'Teste de Titulo',
            'conteudo': 'Conteudo de Teste',
            'autor': 'Autor de Teste',
            'campo_extra': 'valor'
        }
        response = self.client.post(
            self.noticia_url,
            data=json.dumps(payload_com_extras),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())
        self.assertIn('data_publicacao', response.json())
