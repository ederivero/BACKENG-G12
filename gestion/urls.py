from django.urls import path
from .views import (saludar, 
                    CategoriasController, 
                    CategoriaController, 
                    alternarEstadoCategoria, 
                    LibrosController,
                    AutoresController,
                    LibrosAutoresController,
                    mostrarInfoAutor)
# me sirve para indicar un conjunto de rutas estaticas (mostrar generalmente archivos)
from django.conf.urls.static import static
# sirve para obtener los valores de las variables seteadas en el archivo settings.py
from django.conf import settings

urlpatterns = [
    path('', saludar),
    # no es necesario colocar un '/' ya que lo agregara automaticamente Django 
    # as_view > convierte la clase en una vista que django pueda entender (recordemos que Django trabaja con HTML's , en otras palabras con vistas)
    path('categorias', CategoriasController.as_view()),
    path('categoria/<int:id>', CategoriaController.as_view()),
    path('toggle-categoria/<int:id>', alternarEstadoCategoria),
    path('libros', LibrosController.as_view()),
    path('autores', AutoresController.as_view()),
    path('libros-autores',LibrosAutoresController.as_view()),
    path('autor/<int:id>', mostrarInfoAutor),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# agrego todos los archivos en la carpeta 'imagenes' y con la ruta seteada en la variable MEDIA_URL