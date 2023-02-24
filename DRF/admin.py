from django.contrib import admin
from DRF.models import Diretor, Professor, Aluno, Cadeira

class GenericAdmin(admin.ModelAdmin):
    class meta:
        abstract = True
    
    list_display = ('id', 'nome', 'email', 'data_nascimento', 'cpf', 'endereco', 'status',)
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 20

class DiretorAdmin(GenericAdmin):
    pass

admin.site.register(Diretor, DiretorAdmin)

class ProfessorAdmin(GenericAdmin):
    list_display = ('id', 'nome', 'email', 'data_nascimento', 'cpf', 'endereco', 'status', 'cadeiras_cadastradas',)

admin.site.register(Professor, ProfessorAdmin)

class AlunoAdmin(GenericAdmin):
    list_display = ('id', 'nome', 'email', 'data_nascimento', 'cpf', 'endereco', 'status', 'cadeiras_matriculadas',)

admin.site.register(Aluno, AlunoAdmin)

class CadeiraAdmin(admin.ModelAdmin):
    list_display = ('id', 'professor', 'horario', 'limite_de_alunos', 'noticias',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10

admin.site.register(Cadeira, CadeiraAdmin)
