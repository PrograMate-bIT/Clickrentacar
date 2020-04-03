from django.urls import path
from . import frontViews
from .views import UserRegister
from . import views

app_name = 'clickrentacar'

urlpatterns = [
    path('', frontViews.index, name='inicio'),
    path('categorias/', frontViews.categorys, name='categorias'),
    path('categorias/<str:categoria_id>', frontViews.categorys, name='categorias'),
    path('busqueda/', frontViews.search, name='busqueda'),
    path('about/', frontViews.about, name='acerca de'),
    path('contacto/', frontViews.contact, name='contacto'),
    # path('login/', frontViews.user_login, name='iniciar sesion'),
    path('panel/<str:usuario_id>', frontViews.user_panel, name='panel de usuario'),
    path('registro/', UserRegister.as_view(), name='registrarme'),
    path('documentacion-usuario/', frontViews.user_document, name='documento de usuario'),
    path('documentacion-vehiculo/', frontViews.vehicle_document, name='documento de vehiculo'),
    path('alquilar/', frontViews.vehicle_rent, name='alquilar vehiculo'),
    path('publicar/', frontViews.vehicle_publish, name='publicar vehiculo'),
]
