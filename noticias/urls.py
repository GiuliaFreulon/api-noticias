from django.urls import path
from .views import NoticiaDetailView, NoticiaView

urlpatterns = [
    path('noticias/', NoticiaView.as_view(), name='noticia-list-create'),
    path('noticias/<str:id>/', NoticiaDetailView.as_view(), name='noticia-detail'),
]