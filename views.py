# cakes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cake
from .forms import CakeForm

def cake_list(request):
    cakes = Cake.objects.all()
    return render(request, 'cakes/cake_list.html', {'cakes': cakes})

def add_cake(request):
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cake_list')
    else:
        form = CakeForm()
    return render(request, 'cakes/add_cake.html', {'form': form})

def edit_cake(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    if request.method == 'POST':
        form = CakeForm(request.POST, request.FILES, instance=cake)
        if form.is_valid():
            form.save()
            return redirect('cake_list')
    else:
        form = CakeForm(instance=cake)
    return render(request, 'cakes/edit_cake.html', {'form': form, 'cake': cake})

def delete_cake(request, pk):
    cake = get_object_or_404(Cake, pk=pk)
    if request.method == 'POST':
        cake.delete()
        return redirect('cake_list')
    return render(request, 'cakes/delete_cake.html', {'cake': cake})
