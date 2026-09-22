from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProfileForm, CustomUserCreationForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/signup.html', {'form': form})

@login_required
def editar_perfil(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=profile)
        
    return render(request, 'usuarios/perfil.html', {'form': form})


# Ejercicio Nro. 5: Paginado con ListView
class MateriaListView(LoginRequiredMixin, ListView):
    # Si tenés un modelo Materia podés usar: model = Materia
    template_name = 'materias/materia_list.html'
    context_object_name = 'materia_list'
    paginate_by = 5

    def get_queryset(self):
        # Datos de prueba para verificar la paginación sin depender de la BD
        return [
            {'nombre': f'Materia {i}'} for i in range(1, 16)
        ]