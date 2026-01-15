from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from django.http import JsonResponse

def posts_list(request):
    data = [
        {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
        {"userId": 1, "id": 2, "title": "quis ut nam facilis et officia qui", "completed": False}
    ]
    return JsonResponse(data, safe=False)

def comments_list(request):
    data = [
        {"postId": 1, "id": 1, "name": "id labore ex et quam laborum", "email": "Eliseo@gardner.biz", "body": "laudantium enim quasi..."},
    ]
    return JsonResponse(data, safe=False)