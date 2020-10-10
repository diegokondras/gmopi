from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Fornecedor, CategoriaProduto, Produto, Estoque, PessoaFisica, FornecedorPF, Laminadora, Equipamento

admin.site.register(Fornecedor)
admin.site.register(CategoriaProduto)
admin.site.register(Produto)
admin.site.register(Estoque)
admin.site.register(PessoaFisica)
admin.site.register(FornecedorPF)
admin.site.register(Laminadora)
admin.site.register(Equipamento)
