from email import message
from django.shortcuts import get_object_or_404, render, redirect
from LineApp.models import Lineup, Comentario
from django.contrib import messages
from .forms import UserForm, VideoForm,  LoginForm, EditUserForm,SubirAvatarForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.core.paginator import Paginator



def AcercaDe(request):
    return render(request,'LineApp/AcercaDe.html')

def config(request):
    return render(request,'LineApp/config.html')

def perfil(request):
    if request.method== 'POST':
        form = SubirAvatarForm(request.POST)
        if True:
            form.save()
            messages.success(request, f'Imagen actualizada con exito')
            return redirect('perfil')
        else: 
            messages.error(request, f'Ha ocurrido un error con la imagen')
            return redirect('perfil')
    form = SubirAvatarForm()
    data = {"videos": Lineup.objects.filter(usuario=request.user.id).order_by('idLine')[:2],'form':form}
    return render(request,'LineApp/perfil.html', data)

def v_perfil(request):
    data = {"videos": Lineup.objects.filter(usuario=request.user.id).order_by('idLine')}
    return render(request,'LineApp/perfil.html', data)

def  m_perfil(request):
    videos = Lineup.objects.filter(usuario=request.user.id).order_by('idLine')
    data ={
        'videos':videos
    }
    return render (request,'LineApp/listar.html',data)

def ranking(request):
    return render(request,'LineApp/ranking.html')


def registro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            nick1 = form.cleaned_data['username']
            messages.success(request, f'Usuario {nick1} creado con exito')
            return redirect('inicio')
    else:
        form = UserForm()

    contexto = { 'form' : form }

    return render(request,'LineApp/registro.html', contexto)

    # HTML INICIO
def inicio(request):
    lista = Lineup.objects.all().order_by('idLine')
    paginator = Paginator(lista, 12)
    pagina = request.GET.get('page') or 1
    videos = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, paginator.num_pages + 1)
    data = {"lista":videos, "paginas" : paginas, "pagina_actual" : pagina_actual , "comentarios": Comentario.objects.all()}
    return render(request,'LineApp/inicio.html',data)

def filtroAgen(request, agen):
    data = {"lista": Lineup.objects.filter(agente=agen).order_by('idLine')[:16]}
    return render(request,'LineApp/inicio.html', data)

def filtroMapa(request, mapa):
    data = {"lista": Lineup.objects.filter(mapa=mapa).order_by('idLine')[:16]}
    return render(request,'LineApp/inicio.html', data)

def filtroBando(request, band):
    data = {"lista": Lineup.objects.filter(bando=band).order_by('idLine')[:16]}
    return render(request,'LineApp/inicio.html', data)


def subirvideo(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            titulo = form.cleaned_data['titulo']
            messages.success(request, f'Video {titulo} creado con exito')
            return redirect('inicio')
    else:
        form = VideoForm()
    
    contexto = { 'form' : form }
    return render(request,'LineApp/subirvideo.html', contexto)

def editarVideo(request,idLine):
    video = Lineup.objects.get(pk=idLine)
    form = VideoForm(instance=video)

    return render(request,'LineApp/editarvideo.html',{'form':form, 'video':video})

def act_video(request,idLine):
    video = Lineup.objects.get(pk=idLine)
    form = VideoForm(request.POST, instance=video)
    if form.is_valid():
        form.save()
        messages.success(request, 'Video actualizado con exito')
        if request.user.is_staff:
            return redirect(to="listar")
        else:
            return redirect(to="m_perfil")

def InicioSesion(request):
    return render(request,'LineApp/InicioSesion.html')

def editarperfil(request):
    user = User.objects.filter(id=request.user.id).first()
    form = EditUserForm(instance = user)

    return render(request,'LineApp/editarperfil.html',{'form':form, 'user':user})

def act_perfil(request):
    user = User.objects.get(id=request.user.id)
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Perfil actualizado con exito')
        return redirect(to="perfil")

def listar(request):
    videos= Lineup.objects.all()
    data ={
        'videos':videos
    }
    return render (request,'LineApp/listar.html',data)

def eliminar_video(request,idLine):
    videos= Lineup.objects.get(pk=idLine)
    videos.delete()
    videos = Lineup.objects.all()
    messages.success(request, 'Video eliminado con exito')
    if request.user.is_staff:
        return redirect(to="listar")
    else:
        return redirect(to="m_perfil")
    
class CustomLoginView(LoginView):
    template_name = 'LineApp/InicioSesion.html'
    form_class = LoginForm

class like(View):
    def post(self, request, pk, *args, **kwargs):
        post = Lineup.objects.get(pk=pk)

        is_dislike = False
        for dislike in post.dislike.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if is_dislike:
            post.dislike.remove(request.user)

        is_like = False
        for like in post.like.all():
            if like == request.user:
                is_like = True
                break
        
        if not is_like:
            post.like.add(request.user)

        if is_like:
            post.like.remove(request.user)

        next = request.GET.get('next', '/')

        return HttpResponseRedirect(next)

class dislike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Lineup.objects.get(pk=pk)

        is_like = False
        for like in post.like.all():
            if like == request.user:
                is_like = True
                break
        
        if is_like:
            post.like.remove(request.user)

        is_dislike = False
        for dislike in post.dislike.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if not is_dislike:
            post.dislike.add(request.user)

        if is_dislike:
            post.dislike.remove(request.user)

        next = request.GET.get('next', '/')

        return HttpResponseRedirect(next)

def comentar(request, codigo):
    line = Lineup.objects.get(pk=codigo)
    comentario = request.POST['comen']

    Comentario.objects.create(comen=comentario, usuario=request.user, lineUp=line)

    return redirect('inicio')

def borrar_comen (request, codigo):
    usu = Comentario.objects.get(pk=codigo)
    if request.user.is_staff or request.user == usu.usuario:
        comentario = Comentario.objects.get(pk=codigo)
        comentario.delete()
        return redirect('inicio')
    else:
        messages.error(request, 'No tienes permiso para eliminar este comentario')
        return redirect('inicio')