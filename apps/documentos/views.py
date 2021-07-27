from django.shortcuts import render
from django.views.generic import CreateView
from .models import Documento

class DocumentoNovo(CreateView):
    model = Documento
    fields = ['descricao','arquivo']
    #initial = {"descricao": ''}

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(args,kwargs)
        #pegamos o doc de quem pertence e atribuimos ao id que passamos na url
        form.instance.pertence_id = self.kwargs['funcionario_id']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

