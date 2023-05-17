from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # Sólo lectura
    list_display = ('title', 'author', 'published', 'post_categories') # Columnas en la vista previa
    # No se pueden añadir campos Many2Many en esta opción
    ordering = ('author', 'published') # Ordena por autor, y luego por fecha de publicación
    search_fields = ('title', 'content', 'author__username', 'categories__name') # Mostrar un formulario de búsqueda a partir de algunos campos
    date_hierarchy = 'published' # Navega por la parte superior entre fechas
    list_filter = ('author__username', 'categories__name') # Crear una lista al costado

    def post_categories(self, obj): # obj es todos los campos del modelo Post
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    # El for se escribe así porque está accediendo al modelo
    # Accede a las categorías de cada Post
    post_categories.short_description = "Categorías"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)