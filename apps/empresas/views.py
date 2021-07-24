from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']
    def form_valid(self, form):
        #intanciamos o form da empresa antes de salvar
        obj = form.save()
        #pegamos o funcionario logado
        funcionario = self.request.user.funcionario
        #conectamos a relação do funcionario logado a empresa criada
        funcionario.empresa = obj
        #por fim salvamos
        funcionario.save()
        return HttpResponse('ok')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']