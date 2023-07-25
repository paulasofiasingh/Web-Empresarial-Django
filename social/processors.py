from .models import Link

def ctx_dict(request):
    ctx ={}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url # Recorremos cada enlace y creamos un nuevo valor en el diccionario que creamos arriba
        # Los corchetes indican que estamos creando una clave
    return ctx