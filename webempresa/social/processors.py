"""En este punto vamos a crear un procesador de contexto que nos permitirá extender de manera global una variable a través de una función que nos permitirá extender nuestros links de redes sociales sin necesidad de un template y una vista"""


from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx