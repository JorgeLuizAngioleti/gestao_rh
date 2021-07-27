from django.urls import path
from .views import HoraExtraList
urlpatterns = [
path('hora_extra', HoraExtraList.as_view(), name='horas_extras'),
#path('editar/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),

]
