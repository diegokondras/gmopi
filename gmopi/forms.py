from django import forms
from .models import Fornecedor, CategoriaProduto, Produto, MovimentacaoEstoque, Equipamento
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, Reset
from crispy_forms.bootstrap import Accordion, AccordionGroup, Alert, AppendedText, FieldWithButtons, InlineCheckboxes, InlineRadios, PrependedAppendedText, PrependedText, StrictButton, Tab, TabHolder

class ContatoForm(forms.Form):
    emissor = forms.EmailField(required=True, label='Remetente')
    assunto = forms.CharField(required=True)
    msg = forms.CharField(widget=forms.Textarea, label='Mensagem')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('emissor', css_class='form-group col-md-6'),
                Column('assunto', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'msg'
        )
        self.helper.add_input(Submit('submit', 'Enviar'))
        self.helper.add_input(Reset('reset', 'Limpar', css_class='btn-danger float-right'))


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ('tipo', 'nome', 'fornecedor', 'data_aquisicao', 'em_munutencao')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('tipo', css_class='form-group col-md-4'),
                Column('nome', css_class='form-group col-md-8'),
                css_class='form-row'
            ),
            Row(
                Column('fornecedor', css_class='form-group col-md-8'),
                Column('data_aquisicao', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            'em_munutencao',
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger float-right')
            )

        )

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ('nome', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'nome',
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger float-right')
            )
        )

class CategoriaProdutoForm(forms.ModelForm):
    class Meta:
        model = CategoriaProduto
        fields = ('nome',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'nome',
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger float-right')
            )
        )

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'codigo', 'codigo_barras', 'categoria', 'valor_venda', 'custo_medio', 'unidade_medida', 'ncm','cest', 'peso_liquido', 'peso_bruto', 'fornecedor', 'estoque_disponivel', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'estoque_disponivel',
            Row (
                Column('nome', css_class='col-md-8 col-sm-12'),
                Column('categoria', css_class='col-md-4 col-sm-12'),
                css_class='form-row'
            ),
            Row (
                Column('fornecedor', css_class=''),
            ),
            Row (
                Column('codigo', css_class='col-md-4 col-sm-12'),
                Column('codigo_barras', css_class='col-md-8 col-sm-12'),
                css_class='form-row'
            ),
            Row (
                Column('ncm', css_class='col-md-6 col-sm-12'),
                Column('cest', css_class='col-md-6 col-sm-12'),
                css_class='form-row'
            ),
            Row (
                AppendedText('valor_venda', 'R$', active=True, css_class='col-md-6 col-sm-12'),
                AppendedText('custo_medio', 'R$', active=True, css_class='col-md-6 col-sm-12'),
                css_class='form-row'
            ),
            Row (
                Column('unidade_medida', css_class='col-md-4 col-sm-12'),
                Column('peso_liquido', css_class='col-md-4 col-sm-12'),
                Column('peso_bruto', css_class='col-md-4 col-sm-12'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger float-right'),
            )
        )


class MovimentacaoEstoqueForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ('produto', 'tipo_movimentacao', 'quantidade_movimentada', 'data_movimentacao')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row (
                Column('produto', css_class='col-md-8 col-sm-12'),
                Column('tipo_movimentacao', css_class='col-md-4 col-sm-12'),
                css_class='form-row'
            ),
            Row (
                Column('quantidade_movimentada', css_class='col-md-8 col-sm-12'),
                Column('data_movimentacao', css_class='col-md-4 col-sm-12'),
                css_class='form-row'
            ),
            ButtonHolder(
                Submit('submit', 'Salvar', css_class=''),
                Reset('reset', 'Limpar', css_class='btn-danger float-right'),
            )
        )
