from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PedidoForm
from .models import Recipe
from django.urls import reverse_lazy

class RecipeCreatePedido(CreateView):
    form_class = PedidoForm
    template_name = 'recipe/pedido_cliente.html'
    success_url = reverse_lazy('recipes:success_pedido')

    def form_valid(self, form):
        # Guardar los datos del pedido
        pedido = form.save(commit=False)
        pedido.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        # Coloca el request disponible para el formulario
        kwargs = super(RecipeCreatePedido, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class PedidoSuccess(TemplateView):
    template_name = 'recipe/pedido_success.html'


def _crea_diccionario(datos_pedido):
    diccionario = {}
    datos_pedido = datos_pedido[:-1]
    productos = datos_pedido.split("|")
    for producto in productos:
        detalle = producto.split('-')
        diccionario[detalle[0]] = int(detalle[1])
    return diccionario

def realizar_pedido(request):
    pedido = list()
    if request.method == 'POST':
        datos_pedido = request.POST['datos_pedido']
        productos = _crea_diccionario(datos_pedido)
        total = 0
        for codigo_barra in productos.keys():
            cantidad = productos[codigo_barra]
            if cantidad > 0:
                dict_productos = {}
                receta = Recipe.objects.get(pk=codigo_barra)
                dict_productos['id'] = receta.id
                dict_productos['descripcion'] = receta.title
                dict_productos['cantidad'] = cantidad
                dict_productos['precio'] = "100"
                total += cantidad * 100
                pedido.append(dict_productos)
    return render(request, "recipe/detalle_pedido.html", {"pedido": pedido, "total": total})



class RecipesListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe
    # template_name = "recipe/receta_detalle.html"

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('recipes:recipes')

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    # success_url = reverse_lazy('recipes:recipes')

    def get_success_url(self):
        return reverse_lazy('recipes:update', args=[self.object.id]) + '?ok'

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:recipes')
