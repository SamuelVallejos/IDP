from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from django.contrib.auth.models import User

bando = [(-1,"Seleccionar")
        ,(1,"ATK")
        ,(2,"DEF")]

class Lineup (models.Model):
    idLine = models.AutoField(primary_key=True, verbose_name="Id del line up")
    titulo = models.CharField(max_length=50,blank=False,null=False,verbose_name="Titulo del line up")
    agente = models.CharField(max_length=30,blank=False,null=False,verbose_name="Agente del line up")
    mapa = models.CharField(max_length=30,blank=False,null=False,verbose_name="Mapa del line up")
    bando = models.IntegerField(blank=False,null=False,verbose_name="Bando del line up",choices=bando,default=-1)
    descripcion = models.CharField(max_length=200,blank=False,null=False,verbose_name="Descripcion del line up")
    incorporacion = models.CharField(max_length=200,blank=False,null=False,verbose_name="Incorporacion del line up")
    like = models.ManyToManyField(User,blank=True,related_name='likes')
    dislike = models.ManyToManyField(User,blank=True,related_name='dislikes')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion", null=True)
    usuario = UserForeignKey(auto_user_add=True, verbose_name="Usuario")

    def __str__(self):
        return self.titulo

class Comentario (models.Model):
    idComentario = models.AutoField(primary_key=True, verbose_name="Id del comentario")
    comen = models.CharField(max_length=200, blank=False, null=False, verbose_name="Comentario para el line up")
    lineUp = models.ForeignKey(Lineup, on_delete=models.CASCADE)
    usuario = UserForeignKey(auto_user_add=True, verbose_name="Usuario")

    def __str__(self):
        return self.comen

class Avatar (models.Model):
    idAvatar = models.AutoField(primary_key=True, verbose_name="Id del Avatar")
    avatar = models.FileField(unique=True,upload_to = "avatars",null= True)
    usuario = UserForeignKey(auto_user_add=True, verbose_name="Usuario")