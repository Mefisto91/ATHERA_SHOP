from rest_framework import serializers
from ..Models.PrendaModel import PrendaM

class PrendaS(serializers.ModelSerializer):
    class Meta:
        model = PrendaM
        fields = '__all__'





