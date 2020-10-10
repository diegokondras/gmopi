from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

MOVIMENTACOES_CHOICES = [
    ('ENTRADA', 'Entrada'),
    ('SAIDA', 'Saída'),
]

TIPO_EQUIPAMENTO_CHOICES = [
    ('SECADOR', 'Secador'),
    ('TORNO', 'Torno'),
    ('OUTRO', 'Outro'),
]

class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Dimensoes(models.Model):
    espessura = models.CharField(max_length=100, null=True, blank=True)
    comprimento = models.CharField(max_length=100, null=True, blank=True)
    largura = models.CharField(max_length=100, null=True, blank=True)

class Produto(models.Model):
    nome = models.CharField(max_length=100, primary_key=True)
    codigo = models.CharField('Código', max_length=100, blank=True)
    codigo_barras = models.CharField('Código de barras', max_length=150, blank=True)
    categoria = models.ForeignKey('CategoriaProduto', on_delete=models.CASCADE)
    valor_venda = models.CharField('Valor de venda', max_length=10, blank=True)
    custo_medio = models.CharField('Custo médio', max_length=10, blank=True)
    data_cadastro = models.DateField()
    unidade_medida = models.CharField('Unidade de medida', max_length=100, blank=True)
    ncm = models.CharField('NCM', max_length=100, blank=True)
    cest = models.CharField('CEST', max_length=100, blank=True)
    peso_liquido = models.CharField('Peso líquido', max_length=100, blank=True)
    peso_bruto = models.CharField('Peso bruto', max_length=100, blank=True)
    fornecedor = models.ManyToManyField('gmopi.Fornecedor')
    estoque_disponivel = models.PositiveIntegerField(null=True, blank=True)
    estoque_minimo = models.CharField('Estoque mínimo', max_length=10, blank=True)
    estoque_maximo = models.CharField('Estoque máximo', max_length=10,  blank=True)
    data_de_cadastro = models.CharField(max_length=10,  blank=True)

    def __str__(self):
        return self.nome

class Tora(Produto):
    classe = models.CharField(max_length=100)
    diametro = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)

class Lamina(Produto):
    classe = models.CharField(max_length=100)

class Compensado(Produto):
    numero_camadas = models.CharField('Número de camadas', max_length=100)
    dimensoes = models.ForeignKey('Dimensoes', on_delete=models.CASCADE,  null=True, blank=True)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class HistoricoMovimentacaoEstoque(models.Model):
    movimentacao = models.ManyToManyField('gmopi.MovimentacaoEstoque')

class Estoque(models.Model):
    saldo_estoque = models.CharField(max_length=200, null=False, blank=False)
    historico_movimentacao = models.OneToOneField(HistoricoMovimentacaoEstoque, on_delete=models.CASCADE, blank=True)

class MovimentacaoEstoque(models.Model):
    produto  = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False, blank=False)
    tipo_movimentacao = models.CharField(max_length=7, choices=MOVIMENTACOES_CHOICES, null=False, blank=False)
    quantidade_movimentada = models.CharField(max_length=200, null=False, blank=False)
    data_movimentacao = models.CharField(max_length=10,  blank=True)

class Jornada(models.Model):
    jornada = models.CharField(max_length=200, null=False, blank=False)
    descricao = models.CharField('Descrição', max_length=200, null=False, blank=False)
    horario_inicio = models.IntegerField(null=False, blank=False)
    horario_termino = models.CharField(max_length=200, null=False, blank=False)

class Turno(models.Model):
    tipo_turno = models.CharField(max_length=200, null=False, blank=False)

class Turmas(models.Model):
    descricao = models.CharField('Descrição', max_length=200, null=False, blank=False)
    data_inicio = models.DateField('Data de início')


class Contato(models.Model):
    celular = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField('E-mail', max_length=254, null=False, blank=False)
    telefone = models.CharField(max_length=200, null=False, blank=False)
    telefone_comercial = models.CharField(max_length=200, null=False, blank=False)

class Endereco(models.Model):
    rua = models.CharField(max_length=200, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=200, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{}, {}'.format(self.rua, self.numero)

class Equipamento(models.Model):
    tipo = models.CharField(max_length=7, choices=TIPO_EQUIPAMENTO_CHOICES, null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE, null=True, blank=True)
    data_aquisicao = models.DateField('Data de aquisição', null=True, blank=True)
    em_munutencao = models.BooleanField('Em manutenção')

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    contato = models.ForeignKey('Contato', on_delete=models.CASCADE)

    class Meta:
        abstract = True

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=100)

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=25)

class FornecedorPF(PessoaFisica):
    data_inicio = models.DateField()

class FornecedorPJ(PessoaJuridica):
    data_inicio = models.DateField()

class Laminadora(PessoaJuridica):
    contrato = models.ForeignKey('Vigencia', on_delete=models.CASCADE)

class Vigencia(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()

class Contrato(models.Model):
    data_aquisição = models.DateField()
    plano_adquirido = models.CharField(max_length=100)
    dia_vencimento = models.DateField()
    vigencia = models.ForeignKey('Vigencia', on_delete=models.CASCADE)
