from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request, HttpRequest
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import (AllowAny, # cualquiera puede utilizarlo
                                        IsAuthenticated, # Valida que este la token presente y que sea valida
                                        IsAuthenticatedOrReadOnly, # Sera lo mismo que lo anterior PERO si es metodo GET no pedira autenticacion
                                        IsAdminUser, # Verificara si el usuario es is_superuser = True
                                        )
from .models import *
from .serializers import *


class RegistroUsuarioController(APIView):

    @swagger_auto_schema(request_body=RegistroUsuarioSerializer, 
                         operation_description='Registro de un usuario', 
                         operation_summary='Endpoint para registrar un usuario')
    def post(self, request: Request | HttpRequest):
        serializador = RegistroUsuarioSerializer(data= request.data)
        try:
            serializador.is_valid(raise_exception=True)
            nuevoUsuario = Usuario(**serializador.validated_data)

            # generar el hash de la password
            password = serializador.validated_data.get('password')
            nuevoUsuario.set_password(password)

            nuevoUsuario.save()

            return Response(data={
                'message': 'Usuario creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        
        except Exception as err:
            return Response(data={
                'message':'Error al crear el usuario',
                'content':err.args
            },status = status.HTTP_400_BAD_REQUEST)
        
class CategoriasController(APIView):
    # GET | OPTIONS no pedira la token
    permission_classes = [IsAuthenticatedOrReadOnly,]

    @swagger_auto_schema(request_body=CategoriaSerializer, operation_summary='Crear una categoria',)
    def post(self, request: Request | HttpRequest ):
        serializador = CategoriaSerializer(data= request.data)
        try:
            serializador.is_valid(raise_exception=True)

            serializador.save()
            return Response(data={
                'message': 'Categoria creada exitosamente'
            }, status=status.HTTP_201_CREATED)
        
        except Exception as err:
            return Response(data={
                'message':'Error al crear la categoria',
                'content': err.args
            }, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={
        status.HTTP_200_OK: openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'content': openapi.Schema(
                    type=openapi.TYPE_ARRAY, 
                    items=openapi.Items(type=openapi.TYPE_OBJECT, properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, default=0),
                        'nombre': openapi.Schema(type=openapi.TYPE_STRING),
                        'imagen': openapi.Schema(type=openapi.TYPE_INTEGER),})
                )
            }
    )})
    def get(self, request:Request | HttpRequest):
        categorias = Categoria.objects.all()
        serializador = CategoriaSerializer(instance=categorias, many=True)

        return Response(data={
            'content': serializador.data
        })
from rest_framework.parsers import MultiPartParser, FormParser

# Se recomienda usar este método cuando los FILES son ligeros (1MB máximo)
class ProductosController(APIView):
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(request_body=ProductoSerializer, operation_summary='Crear producto')
    def post(self, request: Request | HttpRequest):
        serializador = ProductoSerializer(data=request.data)
        try:
            serializador.is_valid(raise_exception=True)
            serializador.save()
            return Response(data={
                'message': 'Producto creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(data={
                'message':'Error al crear el producto',
                'content': err.args
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(responses={
        status.HTTP_200_OK: openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'content': openapi.Schema(
                    type=openapi.TYPE_ARRAY, 
                    items=openapi.Items(type=openapi.TYPE_OBJECT, properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER, default=0),
                        'nombre': openapi.Schema(type=openapi.TYPE_STRING),
                        'fechaVencimiento': openapi.Schema(type=openapi.TYPE_STRING),
                        'lote': openapi.Schema(type=openapi.TYPE_STRING),
                        'precio': openapi.Schema(type=openapi.TYPE_NUMBER),
                        'categoria': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'imagen': openapi.Schema(type=openapi.TYPE_STRING),})
                )
            }
    )})
    def get(self, request: Request | HttpRequest):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(instance=productos, many=True)
        return Response(data={
            'content': serializer.data
        }, status=status.HTTP_200_OK)

class ProductosSegundoMetodoController(APIView):
    @swagger_auto_schema(request_body=ProductoSegundoMetodoSerializer)
    def post(self, request: Request | HttpRequest):
        serializador = ProductoSegundoMetodoSerializer(data=request.data)
        try:
            serializador.is_valid(raise_exception=True)
            serializador.save()
            return Response(data={
                'message': 'Producto creado exitosamente'
            }, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(data={
                'message':'Error al crear el producto',
                'content': err.args
            }, status=status.HTTP_400_BAD_REQUEST)
        
class UploadImageController(APIView):
    # @swagger_auto_schema()
    def post(self, request: Request | HttpRequest):
        try:
            image = request.FILES.get('imagen')
        except Exception as err:
                return Response(data={
                    'message':'Error al crear el producto',
                    'content': err.args
                }, status=status.HTTP_400_BAD_REQUEST)