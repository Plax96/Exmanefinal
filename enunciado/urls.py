from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar,name="listar"),
    url(r'^grado/crear$', views.crear,name="creargrado"),
    url(r'^materia/$', views.materia,name="materia"),

        ]
