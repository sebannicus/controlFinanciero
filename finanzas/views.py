from django.shortcuts import render, redirect
from .models import Transaccion, Categoria, Usuario

def index(request):
    return render(request, 'index.html')

def listar_transacciones(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'listar_transacciones.html', {'transacciones': transacciones})

def agregar_transaccion(request):
    if request.method == "POST":
        usuario = Usuario.objects.first()  # Usaremos el primer usuario (mejorará después con autenticación)
        tipo = request.POST['tipo']
        monto = request.POST['monto']
        categoria_id = request.POST['categoria']
        fecha = request.POST['fecha']
        descripcion = request.POST['descripcion']

        categoria = Categoria.objects.get(id=categoria_id)

        Transaccion.objects.create(
            usuario=usuario,
            tipo=tipo,
            monto=monto,
            categoria=categoria,
            fecha=fecha,
            descripcion=descripcion
        )
        return redirect('listar_transacciones')

    categorias = Categoria.objects.all()
    return render(request, 'agregar_transaccion.html', {'categorias': categorias})

# Create your views here.
