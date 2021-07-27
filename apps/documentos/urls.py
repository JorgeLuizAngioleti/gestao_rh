from django.urls import path
from .views import  DocumentoNovo


urlpatterns = [
#path('', FucionariosList.as_view(),name='list_funcionarios'),
#path('editar/<int:pk>/', FucionariosEdit.as_view(),name='update_funcionario'),
path('novo_doc/<int:funcionario_id>/', DocumentoNovo.as_view(),name='create_documentos'),
#path('delete/<int:pk>/', FuncionarioDelete.as_view(),name='deletar_funcionario'),

]