from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView

from .forms import FornecedorForm, CategoriaProdutoForm, ProdutoForm, EquipamentoForm, MovimentacaoEstoqueForm
from .models import Fornecedor, CategoriaProduto, Produto, Equipamento, Lamina, Compensado, Tora, Vigencia, Contrato
from django.core.mail import send_mail, BadHeaderError
from .forms import ContatoForm
import logging

from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse

# Tables
from django_tables2 import SingleTableView
from .tables import ProdutoTable, FornecedorTable, EquipamentoTable, CategoriaProdutoTable

# Rest Framework
from rest_framework import generics
from .serializers import ProdutoSerializer, CategoriaProdutoSerializer, EquipamentoSerializer, CompensadoSerializer, LaminaSerializer, ToraSerializer, VigenciaSerializer, ContratoSerializer

# Create your views here.

class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CategoriaProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = CategoriaProdutoSerializer

class EquipamentoList(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = EquipamentoSerializer

class ToraList(generics.ListCreateAPIView):
    queryset = Tora.objects.all()
    serializer_class = ToraSerializer

class CompensadoList(generics.ListCreateAPIView):
    queryset = Compensado.objects.all()
    serializer_class = CompensadoSerializer

class LaminaList(generics.ListCreateAPIView):
    queryset = Lamina.objects.all()
    serializer_class = LaminaSerializer

class VigenciaList(generics.ListCreateAPIView):
    queryset = Vigencia.objects.all()
    serializer_class = VigenciaSerializer

class ContratoList(generics.ListCreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)

def contato(request):
    if request.method == 'GET':
        email_form = ContatoForm()
    else:
        email_form = ContatoForm(request.POST)
        if email_form.is_valid():
            emissor = email_form.cleaned_data['emissor']
            assunto = email_form.cleaned_data['assunto']
            msg = email_form.cleaned_data['msg']

            try:
                send_mail(assunto, msg, emissor, ['diego.ek@aluno.ifsc.edu.br'])
            except BadHeaderError:
                return HttpResponse("Erro =/")
            return redirect('obg')
    return render(request, 'blog/contato.html', {'form': email_form})

def obg(request):
    return HttpResponse("<h2>Obrigado pela mensagem!!!</h2>")

def home(request):
    return render(request, 'home/home.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def fornecedor_new(request):
    if request.method == "POST":
        form = FornecedorForm(request.POST)
        if form.is_valid():
            fornecedor = form.save(commit=False)
            fornecedor.save()
            return redirect('fornecedor_list')
    else:
       form = FornecedorForm()
       return render(request, 'blog/fornecedor_edit.html', {'form': form})

@login_required
def produto_new(request):
     if request.method == "POST":
         form = ProdutoForm(request.POST)
         if form.is_valid():
             produto = form.save(commit=False)
             produto.data_cadastro = timezone.now()
             logger.info("Data de cadastro %s",  produto.data_cadastro)
             produto.save()
             return redirect('produto_list')
     else:
        form = ProdutoForm()
        return render(request, 'produto/produto_edit.html', {'form': form})

@login_required
def categoria_produto_new(request):
     if request.method == "POST":
         form = CategoriaProdutoForm(request.POST)
         if form.is_valid():
             categoria = form.save(commit=False)
             categoria.save()
             return redirect('categoria_produto_list')
     else:
        form = CategoriaProdutoForm()
        return render(request, 'produto/categoria_produto_edit.html', {'form': form})

@login_required
def estoque_new(request):
    if request.method == "POST":
        form = MovimentacaoEstoqueForm(request.POST)
        if form.is_valid():
            estoque = form.save(commit=False)
            estoque.save()
            return render(request, 'blog/estoque_edit.html', {'form': form})
    else:
       form = MovimentacaoEstoqueForm()
       return render(request, 'blog/estoque_edit.html', {'form': form})


def valida_cpf(cpf):
    if len(cpf) < 11:
        return False

    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False

    calc = [i for i in range(1, 10)]
    d1= (sum([int(a)*b for a,b in zip(num[:-2], calc)]) % 11) % 10
    d2= (sum([int(a)*b for a,b in zip(reversed(num[:-2]), calc)]) % 11) % 10
    return str(d1) == num[-2] and str(d2) == num[-1]

def cpf_e_Valido(self, cpf):
    if len(cpf) == 11:
        validador = CPF()
        return validador.validate(cpf)
    else:
        return ValueError("Quantidade de digitos inválida")

@login_required
def cnpj_e_valido(self, cnpj):
    if len(cnpj) == 14:
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(cnpj)
    else:
        return ValueError("Quantidade de digitos inválida")

@login_required
def produto_list(request):
    produtos = Produto.objects.all()
    categorias = CategoriaProduto.objects.all()
    return render(request, 'produto/produto_list.html', {'produtos': produtos, 'categorias': categorias})

@login_required
def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedor/fornecedor_list.html', {'fornecedores': fornecedores})


class EquipamentoView(CreateView):
    form_class = EquipamentoForm
    success_url = reverse_lazy('equipamento_list')
    template_name = 'equipamento/equipamento_edit.html'



class ProdutoListView(SingleTableView):
    model = Produto
    table_class = ProdutoTable
    template_name = 'produto/produto_list.html'


class FornecedorListView(SingleTableView):
    model = Fornecedor
    table_class = FornecedorTable
    template_name = 'fornecedor/fornecedor_list.html'


class EquipamentoListView(SingleTableView):
    model = Equipamento
    table_class = EquipamentoTable
    template_name = 'equipamento/equipamento_list.html'

class CategoriaProdutoListView(SingleTableView):
    model = CategoriaProduto
    table_class = CategoriaProdutoTable
    template_name = 'produto/categoria_produto_list.html'

def produto_chart(request):
    labels = []
    data = []

    queryset = Produto.objects.values('categoriaproduto__nome').annotate(produtos=Sum('estoque_disponivel')).order_by('-produtos')
    for entry in queryset:
        labels.append(entry['categoriaproduto__nome'])
        data.append(entry['produtos'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def pie_chart(request):
    labels = []
    data = []

    queryset = Produto.objects.order_by('-estoque_disponivel')[:5]
    for produto in queryset:
        labels.append(produto.nome)
        data.append(produto.estoque_disponivel)

    return render(request, 'dashboard/pie_chart.html', {
        'labels': labels,
        'data': data,
    })
