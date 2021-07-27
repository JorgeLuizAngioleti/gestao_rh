
from django.views.generic import ListView
from .models import RegistroExtra


class HoraExtraList(ListView):
    model = RegistroExtra
    #fields = ['motivo','horas']
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroExtra.objects.filter(funcionario__empresa=empresa_logada)
