from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Projeto


class ProjetoListView(ListView):
    model = Projeto
    template_name = 'projetos/list.html'
    context_object_name = 'projetos'


class ProjetoDetailView(DetailView):
    model = Projeto
    template_name = 'projetos/detail.html'
    context_object_name = 'projeto'


class ProjetoCreateView(CreateView):
    model = Projeto
    fields = ['usuario', 'titulo', 'descricao', 'imagem', 'link', 'destaque']
    template_name = 'projetos/form.html'
    success_url = reverse_lazy('projeto_list')


class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = ['usuario', 'titulo', 'descricao', 'imagem', 'link', 'destaque']
    template_name = 'projetos/form.html'
    success_url = reverse_lazy('projeto_list')


class ProjetoDeleteView(DeleteView):
    model = Projeto
    template_name = 'projetos/confirm_delete.html'
    success_url = reverse_lazy('projeto_list')