from django.db import models
#importar user pra funcionarios
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    # CASCADE se remover user remove funcionario, PROTEC da de deletar um por vez
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True,blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    @property
    def total_de_hora_extra(self):
        return self.registroextra_set.all().aggregate(Sum('horas'))['horas__sum']
