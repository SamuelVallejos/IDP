from django.contrib import admin
from django.urls import path
from .views import CustomLoginView, borrar_comen,inicio,AcercaDe,perfil,ranking,registro,subirvideo,editarperfil,carrito,listar,eliminar_video, act_perfil, editarVideo, act_video, v_perfil, m_perfil, filtroAgen, filtroMapa, filtroBando, like,dislike,comentar, borrar_comen
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',inicio,name="inicio"),
    path('like/<int:pk>',login_required(like.as_view()),name="like"),
    path('dislike/<int:pk>',login_required(dislike.as_view()),name="dislike"),
    path('comentar/<int:codigo>',login_required(comentar),name="comentar"),
    path('borrar_comen/<int:codigo>',login_required(borrar_comen),name="borrar_comen"),
    path('filtroAgen/<str:agen>',filtroAgen,name="filtroAgen"),
    path('filtroMapa/<str:mapa>',filtroMapa,name="filtroMapa"),
    path('filtroBando/<int:band>',filtroBando,name="filtroBando"),
    path('AcercaDe/',AcercaDe,name="AcercaDe"),
    path('perfil/',login_required(perfil),name="perfil"),
    path('v_perfil/',login_required(v_perfil),name="v_perfil"),
    path('m_perfil/',login_required(m_perfil),name="m_perfil"),
    path('ranking/',ranking,name="ranking"),
    path('registro/',registro,name="registro"),
    path('subirvideo/',login_required(subirvideo),name="subirvideo"),
    path('editarVideo/<int:idLine>',login_required(editarVideo),name="editarVideo"),
    path('act_video/<int:idLine>',login_required(act_video),name="act_video"),
    path('editarperfil/',login_required(editarperfil),name="editarperfil"),
    path('carrito/',carrito,name="carrito"),
    path('act_perfil/',login_required(act_perfil),name="act_perfil"),
    path('listar/',login_required(listar),name="listar"),
    path('eliminar_video/<int:idLine>',login_required(eliminar_video),name="eliminar_video"),
    path('InicioSesion/', CustomLoginView.as_view(), name='InicioSesion'),
    path('logout/', LogoutView.as_view(template_name='LineApp/inicio.html'), name='logout'),
]