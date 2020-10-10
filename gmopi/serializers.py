from rest_framework import serializers
from .models import Produto, Equipamento, CategoriaProduto

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
