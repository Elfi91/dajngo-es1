from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_list, name='users'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
]
