from django.shortcuts import render, redirect
from .models import Dias
from .forms import DiaForm



def display_dias(request):
    dias = Dias.objects.all()
    return render(request, 'dias.html', {'dias': dias})

def form_dias(request):
    
    if request.method == 'POST':
        form = DiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dias_view')
    else:
        form = DiaForm()
    return render(request, 'novo_dia.html', {'form': form})
