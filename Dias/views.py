from django.shortcuts import render, redirect
from .models import Dias
from .forms import DiaForm
from django.views.generic.edit import CreateView, DeleteView



def display_dias(request):
    dias = Dias.objects.all()
    return render(request, 'dias.html', {'dias': dias})

class DiasCreateView(CreateView):
    model = Dias
    fields = ['id', 'data', 'topicos', 'descricao']
    template_name = 'novo_dia.html'
    success_url = '/dias/'


class DiasDeleteView(DeleteView):
    model = Dias
    success_url = '/dias/'