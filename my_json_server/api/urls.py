from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_list, name='posts'), # Rotta per la lista completa
    path('posts/<int:post_id>/', views.post_details, name='posts'), # Rotta dinamica per il singolo post (usiamo int per sicurezza)
    path('comments/', views.comments_list, name='comments'),
    path('albums/', views.albums_list, name='albums'),
    path('photos/', views.photos_lists, name='photos'),
    path('todos/', views.todos_list, name='todos'),
    path('users/', views.users_list, name='users'),
    path('saluta/<str:name>/', views.saluta_nome, name='saluta') # Rotta dinamica: accetta una stringa dall'URL e la passa alla view per generare un saluto personalizzato

]
