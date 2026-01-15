from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_list, name='posts'),
    path('comments/', views.comments_list, name='comments'),
]