from django.urls import path
from . import views
from django.contrib import admin

from django.conf.urls import url
from .views import EquipamentoView, ProdutoListView, FornecedorListView, EquipamentoListView, CategoriaProdutoListView, produto_chart, pie_chart

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fornecedor/new/', views.fornecedor_new, name='fornecedor_new'),
    path('categoriaproduto/new/', views.categoria_produto_new, name='categoria_produto_new'),
    path('produto/new/', views.produto_new, name='produto_new'),
    path('equipamento/new/', EquipamentoView.as_view(), name='equipamento_new'),
    path('estoque/new/', views.estoque_new, name='estoque_new'),
    #path('produto/list/', views.produto_list, name="produto_list"),
    #path('fornecedor/list/', views.fornecedor_list, name="fornecedor_list"),
    path('contato/', views.contato, name='contato'),
    path('contato/obg', views.obg, name='obg'),

    #tables
    path("produto/", ProdutoListView.as_view(), name="produto_list"),
    path("fornecedor/", FornecedorListView.as_view(), name="fornecedor_list"),
    path("equipamento/", EquipamentoListView.as_view(), name="equipamento_list"),
    path("categoria/produto/", CategoriaProdutoListView.as_view(), name="categoria_produto_list"),

    path('produto-chart/', views.produto_chart, name='produto-chart'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
]
