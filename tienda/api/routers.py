from rest_framework.routers import DefaultRouter
from .viewsets import CategoriaViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'productos', ProductoViewSet, basename='productos')