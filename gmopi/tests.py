from django.test import TestCase
from .models import Fornecedor, CategoriaProduto, Produto, Estoque, PessoaFisica, Equipamento, Dimensoes, Compensado, Tora, Lamina, FornecedorPF, FornecedorPJ, Vigencia, Contrato

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

    def test_lamina(self):
        lamina1 = Lamina.objects.get(classe="2")
        self.assertEqual(tora1.classe, "2")

class CompensadoTestCase(TestCase):

    def test_compensado(self):
        comp1 = Compensado.objects.get(numero_camadas="2", dimensoes="")
        self.assertEqual(tora1.numero_camadas, "2")

class FornecedorPFTestCase(TestCase):

    def test_fornecedorpf(self):
        f1 = FornecedorPF.objects.get(data_inicio="28/10/2018")
        self.assertEqual(f1.data_inicio, "28/10/2018")

class FornecedorPJTestCase(TestCase):

    def test_fornecedorpj(self):
        fpj1 = FornecedorPJ.objects.get(data_inicio="28/10/2019")
        self.assertEqual(fpj1.data_inicio, "28/10/2019")

class VigenciaTestCase(TestCase):

    def test_vigencia(self):
        v1 = Vigencia.objects.get(data_inicio="28/10/2019", data_fim="28/10/2021")
        self.assertEqual(v1.data_inicio, "28/10/2019")

class ContratoTestCase(TestCase):

    def test_contrato(self):
        v1 = Contrato.objects.get(data_aquisição="28/10/2019", plano_adquirido="Básico", dia_vencimento="28/10/2021", vigencia="")
        self.assertEqual(v1.plano_adquirido, "Básico")
