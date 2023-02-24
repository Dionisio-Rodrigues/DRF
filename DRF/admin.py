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

class CadeirasCadastradasInline(admin.TabularInline):
    model = Cadeira
    
class ProfessorAdmin(GenericAdmin):
    inlines = [
        CadeirasCadastradasInline,
    ]
    list_display = ('id', 'nome', 'email', 'data_nascimento', 'cpf', 'endereco', 'status', 'cadeiras_cadastradas',)

admin.site.register(Professor, ProfessorAdmin)

class CadeirasEscritasInline(admin.TabularInline):
    model = Cadeira.alunos.through

class AlunoAdmin(GenericAdmin):
    inlines = [
        CadeirasEscritasInline
    ]
    list_display = ('id', 'nome', 'email', 'data_nascimento', 'cpf', 'endereco', 'status', 'cadeiras_escritas')

admin.site.register(Aluno, AlunoAdmin)

class CadeiraAdmin(admin.ModelAdmin):
    list_display = ('id', 'professor', 'horario', 'limite_de_alunos', 'noticias',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10

admin.site.register(Cadeira, CadeiraAdmin)
