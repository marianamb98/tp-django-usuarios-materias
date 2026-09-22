from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('applications.usuarios.urls')),  # <-- Esta línea conecta las rutas de la app
    path('api/', include('tienda.api.urls')),
]