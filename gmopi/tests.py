from django.test import TestCase
from django.test import TestCase
from .models import Fornecedor, CategoriaProduto, Produto, Estoque, PessoaFisica, Equipamento

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
