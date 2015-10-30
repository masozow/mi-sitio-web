from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.listar_publicaciones),
    #url(r'crear/',views.crear_publicaciones)
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_publicaciones),
    url(r'^post/nuevo/$', views.postear_nuevo, name='postear_nuevo'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar_post, name='editar_post'),
]
