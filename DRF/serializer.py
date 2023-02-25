from rest_framework import serializers
from DRF.models import Diretor, Professor, Aluno, Cadeira

class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'nome', 'email', 'cpf', 'endereco', 'status', 'cadeiras_cadastradas']

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'cpf', 'endereco', 'status', 'cadeiras_escritas']

class CadeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadeira
        exclude = ['alunos',]