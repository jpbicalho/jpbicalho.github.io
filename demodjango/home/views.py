from django.shortcuts import render

# Create your views here.

from .models import Mensagem


def index(request):
    mensagens = Mensagem.objects.all()
    return render(request, "home/index.html", {"mensagens": mensagens})

def sobre(request):                                  
    return render(request, "home/sobre.html")