from rest_framework import serializers
from .models import Produto, Equipamento, CategoriaProduto, Contrato, Vigencia, Dimensoes, Tora, Lamina, Compensado

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produto
        fields = '__all__'

class CategoriaProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = CategoriaProduto
        fields = '__all__'

class EquipamentoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Equipamento
        fields = '__all__'


class ContratoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contrato
        fields = '__all__'

class VigenciaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Vigencia
        fields = '__all__'

class ToraSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tora
        fields = '__all__'

class LaminaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lamina
        fields = '__all__'

class CompensadoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Compensado
        fields = '__all__'
