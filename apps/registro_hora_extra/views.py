from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .forms import RegistroHoraExtraForm
from .models import RegistroExtra

class HoraExtraCreate(CreateView):
    model = RegistroExtra
    #fields = ['motivo','funcionario','horas']
    #criar meu proprio form
    form_class = RegistroHoraExtraForm
    #metodo para colocar o user no form
    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user':self.request.user,'teste':'alguma coisa'})
        print(kwargs)
        return kwargs

class HoraExtraList(ListView):
    model = RegistroExtra
    #fields = ['motivo','horas']
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroExtra.objects.filter(funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
    model = RegistroExtra
    #fields = ['motivo','funcionario','horas']
    form_class = RegistroHoraExtraForm

    # metodo para colocar o user no form
    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user, 'teste': 'alguma coisa'})
        print(kwargs)
        return kwargs

class HoraExtraDelete(DeleteView):
    model = RegistroExtra
    success_url = reverse_lazy('horas_extras')