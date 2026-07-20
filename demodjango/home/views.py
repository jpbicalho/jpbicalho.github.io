from django.shortcuts import render

# Create your views here.

from .models import Mensagem
from .forms import MensagemForm


def index(request):
    mensagens = Mensagem.objects.all()
    return render(request, "home/index.html", {"mensagens": mensagens})

def sobre(request):                                  
    return render(request, "home/sobre.html")

def nova_mensagem(request):
    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            mensagem = form.save()

            tags_texto = form.cleaned_data["tags"]
            for pedaco in tags_texto.split(","):
                nome = slugify(pedaco)
                if nome:
                    tag, _ = Tag.objects.get_or_create(nome=nome)
                    mensagem.tags.add(tag)

            return redirect("index")
    else:
        form = MensagemForm()

    return render(request, "home/nova.html", {"form": form})
