from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjetoListView.as_view(), name='projeto_list'),
    path('<int:pk>/', ProjetoDetailView.as_view(), name='projeto_detail'),
    path('novo/', ProjetoCreateView.as_view(), name='projeto_create'),
    path('<int:pk>/editar/', ProjetoUpdateView.as_view(), name='projeto_update'),
    path('<int:pk>/deletar/', ProjetoDeleteView.as_view(), name='projeto_delete'),
]