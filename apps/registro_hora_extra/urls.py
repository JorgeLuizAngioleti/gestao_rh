from django.urls import path
from .views import HoraExtraList, HoraExtraEdit, HoraExtraDelete, HoraExtraCreate, HoraExtraEditVoltarList
urlpatterns = [
path('hora_extra', HoraExtraList.as_view(), name='horas_extras'),
path('editar_hora/<int:pk>/', HoraExtraEdit.as_view(), name='edit_hora_extra'),
path('editar_hora_list/<int:pk>/', HoraExtraEditVoltarList.as_view(), name='edit_hora_extra_list'),
path('deletar_hora/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
path('criar_hora/', HoraExtraCreate.as_view(), name='create_hora_extra'),

]
