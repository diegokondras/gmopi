from django.test import TestCase
from django.test import TestCase
from .models import Fornecedor, CategoriaProduto, Produto, Estoque, PessoaFisica, Equipamento, Dimensoes, Compensado, Tora, Lamina

class ProdutoTestCase(TestCase):
    def setUp(self):
        CategoriaProduto.objects.create(nome="Matéria-prima")
        Produto.objects.create(nome="Trigo", categoria="")
        Produto.objects.create(nome="Tora Pinus", categoria="")

    def test_produto(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

class FornecedorTestCase(TestCase):

    def test_fornecedor(self):
        fornecedor1 = Fornecedor.objects.get(nome="Casan")
        fornecedor2 = Fornecedor.objects.get(nome="Celesc")
        self.assertEqual(fornecedor1.nome, "Casan")
        self.assertEqual(fornecedor2.nome, "Celesc")

class FornecedorTestCase(TestCase):

    def test_fornecedor(self):
        cat1 = CategoriaProduto.objects.get(nome="Matéria-prima")
        cat2 = CategoriaProduto.objects.get(nome="Produto acabado")
        self.assertEqual(cat1.nome, "Matéria-prima")
        self.assertEqual(cat2.nome, "Produto acabado")


class DimensoesTestCase(TestCase):

    def test_dimensoes(self):
        dim1 = Dimensoes.objects.get(espessura="5", comprimento="", largura="")
        dim2 = Dimensoes.objects.get(espessura="6", comprimento="6", largura="")
        self.assertEqual(dim1.espessura, "5")
        self.assertEqual(dim2.comprimento, "6")


class ToraTestCase(TestCase):

    def test_tora(self):
        tora1 = Tora.objects.get(classe="2", diametro="35", idade="8")
        self.assertEqual(tora1.idade, "8")

class LaminaTestCase(TestCase):

    def lamina_tora(self):
        lamina1 = Lamina.objects.get(classe="2")
        self.assertEqual(tora1.classe, "2")

class CompensadoTestCase(TestCase):

    def compensado_tora(self):
        comp1 = Compensado.objects.get(numero_camadas="2", dimensoes="")
        self.assertEqual(tora1.numero_camadas, "2")
