from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Categoria
from .forms import categoriaForm

#Debe manejar tres endpoints diferentes, Registrar Categoria, Obtener todas las categorias en JSON y Vista HTML para mostrar categorias

#metodo que devuelve el JSON
def lista_categorias(request):
    #Obtener todas las instancias del objeto de la BD
    categorias = Categoria.objects.all()

    #Construir una variable en formato de diccionario
    #Porque el JSONResponse lo requiere
    data = [
        {
            #Objeto Categoria construido al aire
            'nombre': c.nombre,
            'imagen': c.imagen,
        }
        for c in categorias
    ]

    #Devolver la respuesta en JSON
    return JsonResponse(data, safe= False)

#Funcion para mandar a la vista del formulario
def agregar_categoria(request):
    #Averiguar si estamos teniendo una respuesta de form
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/categorias/registrar/')#Redirige a la lista de categorias
    #Pintar un formulario vacio
    else:
        form = categoriaForm()
    return render(request,'agregar_c.html',{'form':form})

def lista_categorias_html(request):
    categorias = Categoria.objects.all()
    return render(request,'lista_categorias.html',{'categorias':categorias})