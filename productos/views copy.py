import json
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import Producto
from .forms import productoForm

# Metodo que devuelve el JSON
def lista_productos(request):
    #Obtener todas las instancias del objeto de la BD
    productos = Producto.objects.all()

    #Construir una variable en formato de diccionario
    #Porque el JSONResponse lo requiere
    data = [
        {
            #Objeto Producto construido al aire
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen,
        }
        for p in productos
    ]

    #Devolver la respuesta en JSON
    return JsonResponse(data, safe= False)
#Funcion para mandar a la vista del formulario

def agregar_producto(request):
    #Averiguar si estamos teniendo una respuesta de form
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')#Redirige a la lista de productos
    #Pintar un formulario vacio
    else:
        form = productoForm()
    return render(request,'agregar.html',{'form':form})

#Funcion que registre sin recargar la pagina (sin hacer render)
def registrar_producto(request):
    # Checar que estemos manejando un POST
    if request.method == 'POST':
        try:
            # Intentar obtener los datos del body del request
            data = json.loads(request.body)  # Hace que el parámetro devuelva un JSON
            producto = Producto.objects.create(
                # Básicamente es un constructor
                nombre=data['nombre'],
                precio=data['precio'],
                imagen=data['imagen']
            )  # La función create directamente ingresa el modelo a la BD
            return JsonResponse({'mensaje': 'Registro exitoso', 'id': producto.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)

# Metodo del API PUT
# PUT = Actualizar
def actualizar_producto(request, id_producto):
    if request.method == 'PUT':
        # voy a intentar actualizar
        # 1) paso para obtener la entidad / modelo especifico a actualizar
        # Parametros: modelo y id o identificador
        producto = get_object_or_404(Producto, id=id_producto)
        try:
            #Vamos a actualizar
            # 2) Con la indormacion que deberiamo de estar recibiendo en el cuerpo del request
            data = json.loads(request.body)
            # 3) Actualizar cada campo disponible de la entidad
            producto.nombre = data.get('nombre', producto.nombre)
            producto.precio = data.get('precio', producto.precio)
            producto.imagen = data.get('imagen', producto.imagen)
            # 4) Guardar los cambios
            producto.save()
            # 5) Devolver una respuesta exitosa
            return JsonResponse({'mensaje': 'Producto actualizado correctamente'}, status=200)
        except Exception as e:
            # 6) Devolver una respuesta de error
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)


#El metodo del API DELETE
def borrar_producto(request, id_producto):
    if request.method == ' DELETE':
        producto = get_object_or_404(Producto, id=id_producto)
        producto.delete() # <!--- estp borra fisicamente de la base de datos
        return JsonResponse({'mensaje': 'Producto eliminado correctamente'}, status=200)
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)

# Metodo que devuela solo 1 objeto de la BD
def obtener_producto(request, id_producto):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id_producto)
        data = {
            'nombre': producto.nombre,
            'precio': producto.precio,
            'imagen': producto.imagen,
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)


