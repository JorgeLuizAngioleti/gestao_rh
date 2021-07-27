from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Departamento

class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        # pegar funcionario da empresa logada
        empresa_logaga = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logaga)

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        #no campo empresa salvamos a empresa logada
        departamento.empresa=self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')

class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']