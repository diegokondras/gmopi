import django_tables2 as tables
from .models import Produto, Fornecedor, Equipamento, CategoriaProduto

class ProdutoTable(tables.Table):
    class Meta:
        model = Produto
        template_name = "django_tables2/bootstrap.html"
        fields = ("nome", "codigo", "codigo_barras", "categoria", "valor_venda", "custo_medio", "unidade_medida", "ncm","cest", "peso_liquido", "peso_bruto", "fornecedor", )

class FornecedorTable(tables.Table):
    class Meta:
        model = Fornecedor
        template_name = "django_tables2/bootstrap.html"
        fields = ("nome", )

class EquipamentoTable(tables.Table):
    class Meta:
        model = Equipamento
        template_name = "django_tables2/bootstrap.html"
        fields = ('tipo', 'nome', 'fornecedor', 'data_aquisicao', 'em_munutencao', 'editar', 'excluir')

class CategoriaProdutoTable(tables.Table):
    class Meta:
        model = CategoriaProduto
        template_name = "django_tables2/bootstrap.html"
        fields = ('nome',)
