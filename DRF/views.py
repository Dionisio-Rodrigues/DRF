from rest_framework import viewsets
from DRF.models import Diretor, Professor, Aluno, Cadeira
from DRF.serializer import DiretorSerializer, ProfessorSerializer, AlunoSerializer, CadeiraSerializer

class DiretoresViewSet(viewsets.ModelViewSet):
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer

class ProfessoresViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CadeirasViewSet(viewsets.ModelViewSet):
    queryset = Cadeira.objects.all()
    serializer_class = CadeiraSerializer