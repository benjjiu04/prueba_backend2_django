from django.forms import ModelForm, TextInput, NumberInput, DateInput
from catalogo.models import Producto

class ProductoForm(ModelForm):

  class Meta:

    model = Producto
    fields = [
      "nombre",
      "categoria",
      "precio",
      "stock",
      "sku",
      "fecha_ingreso"
    ]

    widgets = {
      "nombre": TextInput(attrs={"type": "text",
                                "class": "form-control"}),
      
      "precio": NumberInput(attrs={"type": "number",
                                   "class": "form-control"}),

      "stock": NumberInput(attrs={"type": "number",
                                  "class": "form-control"}),

      "sku": NumberInput(attrs={"type": "number",
                                "class": "form-control"}),

      "fecha_ingreso": DateInput(attrs={"type": "date",
                                "class": "form-control"})
    }