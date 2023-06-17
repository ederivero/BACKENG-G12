# https://www.django-rest-framework.org/api-guide/serializers/
from rest_framework import serializers
from .models import Categoria, Libro, Autor

class CategoriaSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    class Meta:
        model = Categoria
        # sirve para indicar que campos del modelos queremos usar
        # fields = ['id', 'nombre']
        # exclude = ['nombre', 'piso'] # utilizar todos los campos excepto el nombre y el piso
        fields = '__all__' 
    

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    # write_only > le digo que esta columna o campo solo sera requerida para cuando se quiera hacer la escritura (grabar) y no para devolver al cliente
    libros = serializers.ListField(child=serializers.IntegerField(), allow_empty = True, required=False, write_only=True)

    class Meta:
        model = Autor
        fields = '__all__'