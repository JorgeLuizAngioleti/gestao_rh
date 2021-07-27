from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import( ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView)
from .models import Funcionario


class FucionariosList(ListView):
    model = Funcionario
    #metodo para listar
    def get_queryset(self):
        # pegar funcionario da empresa logada
        empresa_logaga = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logaga)

#atualizar
class FucionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']

#deletar
class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']
    #manipular formularios
    def form_valid(self, form):
        funcionario = form.save(commit=False)
        #cria um username concatenando primeiro e segundo nome digitado, split remove os espaços
        username = funcionario.nome.split(' ')[0]+funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa#cria uma empresa do mesmo que o usuario logado
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)

