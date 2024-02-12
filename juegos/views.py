from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def juegos(request):     
    juegos = Detalles.objects.all().order_by('juego__nombre')
    
    paginator = Paginator(juegos, 24)
    page = request.GET.get('page', 1)
    
    try:
        juegos_paginados = paginator.page(page)
    except PageNotAnInteger:
        juegos_paginados = paginator.page(1)
    except EmptyPage:
        juegos_paginados = paginator.page(paginator.num_pages)
    
    return render(request, 'home.html', {'juegos': juegos_paginados})


def buscar(request):
    if request.method == 'POST':
        txt = request.POST['txt']
        juegos = Detalles.objects.filter(juego__nombre__icontains=txt).order_by('juego__nombre')
        return render(request, 'buscar.html', {'juegos': juegos, 'txt':txt})
    else:
        return redirect(request, 'home.html')
        
    
    
    