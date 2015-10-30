from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear
from .forms import PostearFormulario
from django.shortcuts import redirect
# Create your views here.
def listar_publicaciones(request):
    publicaciones=Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request,'blog/listar_publicaciones.html',{'publicaciones':publicaciones})
    #Lo que va dentro de las llaves: {'nombre de variable que va a recibir en la pagina web':nombre de lo que se va a enviar}

def detalle_publicaciones(request, pk):
    #se iguala el parametro "pk" de la funcion, con la "pk" del modelo,
    #la cual se genera automaticamente en todos los modelos
    #publicacion=Postear.objects.filter(pk=pk)
    #se usa get_object_or_404 para capturar los errores y poder redirigir a una pagina de error personalizada
    publicacion=get_object_or_404(Postear,pk=pk)
    return render (request,'blog/detalle_publicaciones.html',{'publicaciones':publicacion})

def postear_nuevo(request):
    if request.method == "POST":
        form = PostearFormulario(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_publicaciones', pk=post.pk)
    else:
        form = PostearFormulario()
    return render(request, 'blog/editar_post.html', {'form': form})

def editar_post(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        form = PostearFormulario(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_publicaciones', pk=post.pk)
    else:
        form = PostearFormulario(instance=post)
    return render(request, 'blog/editar_post.html', {'form': form})
