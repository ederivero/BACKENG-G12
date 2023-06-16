from django.urls import path
from .views import saludar, CategoriasController, CategoriaController

urlpatterns = [
    path('', saludar),
    # no es necesario colocar un '/' ya que lo agregara automaticamente Django 
    # as_view > convierte la clase en una vista que django pueda entender (recordemos que Django trabaja con HTML's , en otras palabras con vistas)
    path('categorias', CategoriasController.as_view()),
    path('categoria/<int:id>', CategoriaController.as_view()),
]