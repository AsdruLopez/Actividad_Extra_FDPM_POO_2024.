# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Libro
# from .forms import LibroForm

# def listar_libros(request):
#     libros = Libro.objects.all()
#     return render(request, 'libros/listar_libros.html', {'libros': libros})

# def crear_libro(request):
#     if request.method == 'POST':
#         form = LibroForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_libros')
#     else:
#         form = LibroForm()
#     return render(request, 'libros/crear_libro.html', {'form': form})

# def actualizar_libro(request, pk):
#     libro = get_object_or_404(Libro, pk=pk)
#     if request.method == 'POST':
#         form = LibroForm(request.POST, instance=libro)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_libros')
#     else:
#         form = LibroForm(instance=libro)
#     return render(request, 'libros/crear_libro.html', {'form': form})

# def eliminar_libro(request, pk):
#     libro = get_object_or_404(Libro, pk=pk)
#     if request.method == 'POST':
#         libro.delete()
#         return redirect('listar_libros')
#     return render(request, 'libros/eliminar_libro.html', {'libro': libro})


from django.shortcuts import render

def listar_libros(request):
    return render(request, 'libros/listar_libros.html')

def crear_libro(request):
    return render(request, 'libros/crear_libro.html')  # Asegúrate de que esta plantilla exista
