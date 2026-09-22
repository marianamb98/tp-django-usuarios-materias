from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from tienda.models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'categoria': ['exact'],
        'precio': ['gte', 'lte'],
        'stock': ['gte'],
    }
    search_fields = ['nombre']
    ordering_fields = ['precio', 'stock', 'nombre']
    ordering = ['nombre']

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {'error': 'Solo administradores pueden eliminar productos.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['get'], url_path='sin-stock')
    def sin_stock(self, request):
        qs = Producto.objects.filter(stock=0)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='por-categoria')
    def productos_por_categoria(self, request):
        nombre_cat = request.query_params.get('categoria', None)
        if not nombre_cat:
            return Response(
                {'error': 'Debe proporcionar el parámetro ?categoria=<nombre>'},
                status=status.HTTP_400_BAD_REQUEST
            )
        qs = Producto.objects.filter(categoria__nombre__iexact=nombre_cat)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)