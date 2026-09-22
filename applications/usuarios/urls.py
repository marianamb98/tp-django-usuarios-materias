from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import register, editar_perfil, MateriaListView

urlpatterns = [
    path('signup/', register, name='signup'),
    path('login/', LoginView.as_view(template_name='usuarios/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('perfil/', editar_perfil, name='perfil'),
    path('materias/', login_required(MateriaListView.as_view()), name='materias_list'),
]