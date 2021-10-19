from django.urls import path
from .views import RecipesListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView, RecipeCreatePedido, PedidoSuccess
from .import views

recipe_patterns = ([
    path('', RecipesListView.as_view(), name="recipes"),
    path('<int:pk>/<slug:recipe_slug>/', RecipeDetailView.as_view(), name="recipe"),
    path('create/', RecipeCreateView.as_view(), name="create"),
    path('update/<int:pk>', RecipeUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', RecipeDeleteView.as_view(), name="delete"),
    path('pedido/', views.realizar_pedido, name="detalle_pedido"),
    path('create_pedido/', RecipeCreatePedido.as_view(), name="create_pedido"),
    path('success_pedido/', PedidoSuccess.as_view(), name="success_pedido"),
    path('pedido/', views.realizar_pedido, name="detalle_pedido"),

], 'recipes')