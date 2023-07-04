
from django.shortcuts import render, redirect
from .forms import AutoEspacioForm, TarifaForm, EspacioForm, IngresoForm, EgresoForm
from .models import EspacioEstacionamiento,Ingreso
from django.contrib import messages
from datetime import date


def home_view (request):
    espacios = EspacioEstacionamiento.objects.all()
    contexto= {
        'espacios' : espacios
    }
    return render(request,'SystemParking/estacionamientos.html',contexto)


def registro_auto_espacio(request):
    if request.method == 'POST':
        form = AutoEspacioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page-home')  # Redirecciona a la vista deseada después de guardar el formulario
    else:
        form = AutoEspacioForm()
    return render(request, 'SystemParking/form.html', {'form': form})


def detalles_view(request):
    tarifa_form = TarifaForm(request.POST or None)
    espacio_form = EspacioForm(request.POST or None)
    espacios = EspacioEstacionamiento.objects.all()

    context = {
        'tarifa_form': tarifa_form,
        'espacio_form': espacio_form,
        'espacios': espacios
    }

    return render(request, 'SystemParking/detalles.html', context)


def registro_tarifa (request):
    if request.method == 'POST':
        form = TarifaForm(request.POST)
        if form.is_valid():
            messages.success(request,'Se ha guardado correctamente la tarifa')
            print(messages)
            form.save()
            return redirect('page-detalles')
    else:
        form = TarifaForm()

    context = {
        'form': form
    }

    return render(request,'SystemParking/nueva-tarifa.html',context)


def registro_espacio (request):
    if request.method == 'POST':
        form = EspacioForm(request.POST)
        if form.is_valid():
            messages.success(request,'Se ha guardado correctamente el nuevo espacio')
            form.save()
            return redirect('page-detalles')
    else:
        form = EspacioForm()

    context = {
        'form': form
    }

    return render(request,'SystemParking/nuevo-espacio.html',context)


def view_contable_home(request):
    ingresos = Ingreso.objects.all()
    contexto={
        'ingresos': ingresos
    }

    return render(request,'SystemParking/contable-home.html',contexto)


def registro_ingreso(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)  # Guardar el formulario sin guardar en la base de datos
            ingreso.fechaCreacion = date.today()  # Asignar la fecha actual al campo fechaCreacion
            ingreso.save()  # Guardar el objeto ingreso en la base de datos
            messages.success(request,'Registro exitoso')
            return redirect('page-contable')  # Redireccionar a una página exitosa después de guardar los datos
    else:
        form = IngresoForm()

    return render(request, 'SystemParking/nuevo-ingreso.html', {'form': form})