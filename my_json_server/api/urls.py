from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_list, name='posts'),
    path('comments/', views.comments_list, name='comments'),
    path('albums/', views.albums_list, name='albums'),
    path('photos/', views.photos_lists, name='photos'),
    path('todos/', views.todos_list, name='todos'),
    path('users/', views.users_list, name='users')
]