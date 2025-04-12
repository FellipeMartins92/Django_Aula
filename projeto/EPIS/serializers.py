from rest_framework import serializers
from .models import *

class EPISerializer(serializers.ModelSerializer):
    class Meta:
        model = EPI
        fields = '__all__'

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'

class Tipo_EPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_EPI
        fields = '__all__'        