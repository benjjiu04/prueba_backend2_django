from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from catalogo.models import Producto, Categoria
from catalogo.forms import ProductoForm

def es_administrador(user):
    """Auxiliar para verificar si el usuario tiene rol Administrador"""
    return user.is_staff or user.is_superuser or user.groups.filter(name='Administrador').exists()

def index(request: HttpRequest) -> HttpResponse:
    categorias_productos = Categoria.objects.all()
    productos_registrados = Producto.objects.all()
    return render(request, "catalogo/index.html", {
        "categorias_productos": categorias_productos,
        "productos_registrados": productos_registrados
    })

def catalogo(request: HttpRequest) -> HttpResponse:
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')

    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    categorias = Categoria.objects.all()

    context = {
        "productos": productos,
        "categorias": categorias,
    }
    return render(request, "catalogo/catalogo.html", context)

@login_required
def admin_panel(request: HttpRequest) -> HttpResponse:
    productos = Producto.objects.all()
    return render(request, "catalogo/admin_panel.html", {"productos": productos})

@login_required
def producto_crear(request: HttpRequest) -> HttpResponse:
    # Bloqueo en backend para perfil Asistente
    if not es_administrador(request.user):
        return HttpResponseForbidden("No posees permisos de Administrador para crear productos.")

    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_panel")
    else:
        form = ProductoForm()

    return render(request, "catalogo/producto_form.html", {"form": form})

@login_required
def producto_editar(request: HttpRequest, pk: int) -> HttpResponse:
    # Bloqueo en backend para perfil Asistente
    if not es_administrador(request.user):
        return HttpResponseForbidden("No posees permisos de Administrador para editar productos.")

    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("admin_panel")
    else:
        form = ProductoForm(instance=producto)

    return render(request, "catalogo/producto_form.html", {
        "form": form,
        "producto": producto
    })

@login_required
def producto_eliminar(request: HttpRequest, pk: int) -> HttpResponse:
    # Bloqueo en backend para perfil Asistente
    if not es_administrador(request.user):
        return HttpResponseForbidden("No posees permisos de Administrador para eliminar productos.")

    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        producto.delete()
        return redirect("admin_panel")

    return render(request, "catalogo/producto_confirm_delete.html", {"producto": producto})