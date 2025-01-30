from django.urls import path
from . import views

urlpatterns = [
    path('noticias/adicionar/', views.adicionar_noticia, name='adicionar-noticia'),
    path('noticias/', views.listar_todas_noticias, name='noticia-list'),
    path('noticias/<str:id>/', views.obter_noticia, name='noticia-detail'),
    path('noticias/editar/<str:id>/', views.editar_noticia, name='editar-noticia'),
    path('noticias/remover/<str:id>/', views.remover_noticia, name='remover-noticia'),
]