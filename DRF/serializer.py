from rest_framework import serializers
from DRF.models import Diretor, Professor, Aluno, Cadeira

class DiretorSerializer(serializers.ModelSerializer):
    class meta:
        model = Diretor
        