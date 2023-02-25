from django.urls import path, include
from DRF.views import DiretoresViewSet, ProfessoresViewSet, AlunosViewSet, CadeirasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('diretor', DiretoresViewSet, basename='Diretor')
router.register('alunos', AlunosViewSet, basename='Aluno')

urlpatterns = [
    path('', include(router.urls))
]
