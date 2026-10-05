from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Rutas públicas
    path('', views.index, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),

    # Autenticación (Login / Logout)
    path('login/', auth_views.LoginView.as_view(template_name='catalogo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Panel de Administración Privado
    path('panel/', views.admin_panel, name='admin_panel'),

    # Operaciones CRUD para Productos
    path('producto/crear/', views.producto_crear, name='producto_crear'),
    path('producto/<int:pk>/editar/', views.producto_editar, name='producto_editar'),
    path('producto/<int:pk>/eliminar/', views.producto_eliminar, name='producto_eliminar'),
]