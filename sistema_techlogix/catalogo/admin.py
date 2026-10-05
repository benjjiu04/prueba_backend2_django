from django.contrib import admin
from catalogo.models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'categoria', 'precio', 'stock', 'fecha_ingreso')
    list_filter = ('categoria', 'fecha_ingreso')
    search_fields = ('nombre', 'sku')