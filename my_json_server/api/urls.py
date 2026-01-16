from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_index, name='api_index'), # Rotta per la lista completa di tutti i dati
    path('posts/', views.posts_list, name='posts'), # Rotta per la lista completa
    path('posts/<int:post_id>/', views.post_details, name='post_details'), # Rotta dinamica per il singolo post (usiamo int per sicurezza)
    path('posts/user/<int:user_id>/', views.user_posts, name='user_posts'), # Rotta dinamica per il singolo utente (usiamo int per sicurezza)
    path('comments/', views.comments_list, name='comments'),
    path('albums/', views.albums_list, name='albums'),
    path('photos/', views.photos_lists, name='photos'),
    path('todos/', views.todos_list, name='todos'),

    path('saluta/<str:name>/', views.saluta_nome, name='saluta') # Rotta dinamica: accetta una stringa dall'URL e la passa alla view per generare un saluto personalizzato

]
