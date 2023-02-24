from django.db import models

class Associado(models.Model):
    class meta:
        abstract = True

    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=100)
    status = models.BooleanField()

    def __str__(self):
        return self.nome

class Diretor(Associado):
    pass

class Professor(Associado):
    pass
    # cadeiras_cadastradas = models.ManyToOneRel(field = Cadeira.professor,to = 'Cadeira', field_name='cadeiras_cadastradas', related_name='professor')

# FIXME: Implementar campo foto
class Aluno(Associado):
    cadeiras_matriculadas = models.ManyToManyField('Cadeira',)
    # foto = models.ImageField()
    semestre = models.IntegerField()

# FIXME: Implementar campos: ap1, ap2, ap3, entregra_de_prova, material_de_alunos
class Cadeira(models.Model):
    professor = models.ForeignKey(Professor, related_name='cadeiras_cadastradas', on_delete=models.SET_NULL, null=True)
    horario = models.TimeField()
    limite_de_alunos = models.IntegerField()
    # ap1 = models.FileField()
    # ap2 = models.FileField()
    # ap3 = models.FileField()
    # entrega_de_prova = models.FileField()
    noticias = models.TextField()
    # material_de_alunos = models.FileField()
    
