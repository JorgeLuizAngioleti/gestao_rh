from django.forms import ModelForm
from .models import RegistroExtra
from apps.funcionarios.models import Funcionario

class RegistroHoraExtraForm(ModelForm):
    #metodo abaixo altera o form,passei o user para filtrar
    def __init__(self, user,teste, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args,**kwargs)
        #sobreescrever o campo funcionario
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa)
        print(teste)
    class Meta:
        model = RegistroExtra
        fields = ['motivo','funcionario','horas']