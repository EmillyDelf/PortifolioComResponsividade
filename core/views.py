from django.shortcuts import render
from projetos.models import Projeto

def home(request):
    projetos = Projeto.objects.all()
    return render(request, 'base.html', {'projetos': projetos})