from django.db.models import (Model, CharField, IntegerField, 
                             ForeignKey, TextField, DateField,
                             CASCADE)

# Create your models here.

class Categoria(Model):
  
  nombre = CharField(verbose_name="tipo de categoria", max_length=250)
  descripcion = TextField(default="placeholder", verbose_name="descripción del producto", blank=True, null=True)

class Producto(Model):

  nombre = CharField(verbose_name="nombre del producto", max_length=250)
  categoria = ForeignKey(Categoria, on_delete=CASCADE, null=True, blank=True)
  precio = IntegerField(verbose_name="precio del producto")
  stock = IntegerField(verbose_name="cantidad en stock")
  sku = IntegerField(verbose_name="codigo de referencia del producto")
  fecha_ingreso = DateField()


  
