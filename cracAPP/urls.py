from django.urls import path
from . import FrontViews
from .views import UserRegister
from . import views

app_name = 'clickrentacar'

urlpatterns = [
    path('', FrontViews.index, name='inicio'),
    path('categorias/', FrontViews.categorys, name='categorias'),
    path('categorias/<str:categoria_id>', FrontViews.categorys, name='categorias'),
    path('busqueda/', FrontViews.search, name='busqueda'),
    path('about/', FrontViews.about, name='acerca de'),
    path('contacto/', FrontViews.contact, name='contacto'),
    #path('login/', FrontViews.user_login, name='iniciar sesion'),
    path('panel/<str:usuario_id>', FrontViews.user_panel, name='panel de usuario'),
    path('registro/', UserRegister.as_view(), name='registrarme'),
    path('documentacion-usuario/', FrontViews.user_document, name='documento de usuario'),
    path('documentacion-vehiculo/', FrontViews.vehicle_document, name='documento de vehiculo'),
    path('alquilar/', FrontViews.vehicle_rent, name='alquilar vehiculo'),
    path('publicar/', FrontViews.vehicle_publish, name='publicar vehiculo'),
]
