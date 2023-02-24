from rest_framework import serializers
from DRF.models import Diretor, Professor, Aluno, Cadeira

class DiretorSerializer(serializers.ModelSerializer):
    class meta:
        model = Diretor
        fields = ['id', 'nome', 'email', 'cpf', 'endereco', 'status']

class ProfessorSerializer(serializers.ModelSerializer):
    class meta:
        model = Professor
        fields = ['id', 'nome', 'email', 'cpf', 'endereco', 'status', 'cadeiras_cadastradas']

class AlunoSerializer(serializers.ModelSerializer):
    class meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'cpf', 'endereco', 'status', 'cadeiras_escritas']

class CadeiraSerializer(serializers.ModelSerializer):
    class meta:
        model = Cadeira
        fields = ['id', 'professor', 'horario', 'limite_de_alunos', 'noticias']