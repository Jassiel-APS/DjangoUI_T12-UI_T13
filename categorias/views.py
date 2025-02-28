from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import Categoria
from .forms import categoriaForm
import json

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

def registrar_c(request):
    # Checar que estemos manejando un POST
    if request.method == 'POST':
        try:
            # Intentar obtener los datos del body del request
            data = json.loads(request.body)  # Hace que el parámetro devuelva un JSON
            categoria = Categoria.objects.create(
                # Básicamente es un constructor
                nombre=data['nombre'],
                imagen=data['imagen']
            )  # La función create directamente ingresa el modelo a la BD
            return JsonResponse({'mensaje': 'Registro exitoso', 'id': categoria.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)
