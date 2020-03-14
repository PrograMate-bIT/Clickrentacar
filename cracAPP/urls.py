from django.urls import path

from . import views

app_name = 'clickrentacar'

urlpatterns = [
    path('', views.index, name='inicio'),
    path('categorias/<str:categoria_id>', views.categorias, name='categorias'),
    path('busqueda/', views.search, name='busqueda'),
    path('acerca-de/', views.about, name='acerca de'),
    path('contacto/', views.contact, name='contacto'),
    path('iniciar-sesion/', views.userLogin, name='iniciar sesion'),
    path('panel-usuario/<str:usuario_id>', views.userPanel, name='panel de usuario'),
    path('registro/', views.userRegister, name='registrarme'),
    path('documentacion-usuario/', views.userDocument, name='documento de usuario'),
    path('documentacion-vehiculo/', views.vehicleDocument, name='documento de vehiculo'),
    path('alquilar-vehiculo/', views.vehicleRent, name='alquilar vehiculo'),
    path('publicar-vehiculo/', views.vehiclePublish, name='publicar vehiculo'),
    ]
