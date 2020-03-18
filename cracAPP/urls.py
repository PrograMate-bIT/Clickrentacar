from django.urls import path

from . import views

app_name = 'clickrentacar'

urlpatterns = [
    path('', views.index, name='inicio'),
    path('categorias/', views.categorys, name='categorias'),
    path('categorias/<str:categoria_id>', views.category_id, name='categorias'),  # name='<categoria_id>),
    path('busqueda/', views.search, name='busqueda'),
    path('about/', views.about, name='acerca de'),
    path('contacto/', views.contact, name='contacto'),
    path('login/', views.user_login, name='iniciar sesion'),
    path('panel/<str:usuario_id>', views.user_panel, name='panel de usuario'),
    path('registro/', views.user_register, name='registrarme'),
    path('documentacion-usuario/', views.user_document, name='documento de usuario'),
    path('documentacion-vehiculo/', views.vehicle_document, name='documento de vehiculo'),
    path('alquilar/', views.vehicle_rent, name='alquilar vehiculo'),
    path('publicar/', views.vehicle_publish, name='publicar vehiculo'),
]
