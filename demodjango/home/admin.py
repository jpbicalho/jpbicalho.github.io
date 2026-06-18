from django.contrib import admin

# Register your models here.


from .models import Mensagem
from .models import Categoria


@admin.register(Categoria)                                       # ← novo
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)


@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "criada_em")
    search_fields = ("titulo", "conteudo")
