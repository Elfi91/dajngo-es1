from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from django.http import JsonResponse

def api_index(request):
    return JsonResponse({
        "project": "JSONPlaceholder Clone API",
        "version": "1.0.0",
        "author": "Elisabetta Fino",
        "endpoint_disponibili": {
            "posts": "api/posts/",
            "comments": "api/comments/",
            "albums": "api/albums/",
            "photos": "api/photos/",
            "todos": "api/todos/",

        },
        })

POSTS_DATA = [
        {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    },
    {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    }
    ]

def posts_list(request):
    return JsonResponse(POSTS_DATA, safe=False)

def post_details(request, post_id):
    post_trovato = None
    for p in POSTS_DATA:
        if str(p['id']) == str(post_id):
            post_trovato = p
            break
    
    if post_trovato:
        return JsonResponse(post_trovato)
    return JsonResponse({"errore": "Post non trovato"}, status=404)

def comments_list(request):
    data = [
        {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    },
    {
    "postId": 1,
    "id": 2,
    "name": "quo vero reiciendis velit similique earum",
    "email": "Jayne_Kuhic@sydney.com",
    "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
    },
    ]
    return JsonResponse(data, safe=False)

def albums_list(request):
    data = [
    {
    "userId": 1,
    "id": 7,
    "title": "quibusdam autem aliquid et et quia"
    },
    {
    "userId": 1,
    "id": 8,
    "title": "qui fuga est a eum"
    },
    ]
    return JsonResponse(data, safe=False)

def photos_lists(request):
    data = [
    {
    "albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"
    },
    {
    "albumId": 1,
    "id": 2,
    "title": "reprehenderit est deserunt velit ipsam",
    "url": "https://via.placeholder.com/600/771796",
    "thumbnailUrl": "https://via.placeholder.com/150/771796"
    },
    ]
    return JsonResponse(data, safe=False)

def todos_list(request):
    data = [
    {
    "userId": 1,
    "id": 7,
    "title": "illo expedita consequatur quia in",
    "completed": False
    },
    {
    "userId": 1,
    "id": 8,
    "title": "quo adipisci enim quam ut ab",
    "completed": True
    },
    ]
    return JsonResponse(data, safe=False)



# Questa funzione serve per la rotta saluta/<str:name>/
def saluta_nome(request, name):
    messaggio = f"Ciao {name}, benvenuto/a nella tua rotta dinamica"
    return JsonResponse({'messaggio': messaggio})

# Questa funzione serve per la rotta posts/user/<int:user_id>/
def user_posts(request, user_id):
    # Filtriamo i post della lista globale POSTS_DATA
    filtrati = [p for p in POSTS_DATA if p['userId'] == user_id]
    return JsonResponse(filtrati, safe=False)