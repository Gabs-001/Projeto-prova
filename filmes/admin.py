from django.contrib import admin
from .models import Generos, Filmes
from rest_framework.authtoken.models import Token

# Admin para o modelo Generos: mostra o campo 'nome' e permite busca por nome
@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
   list_display = ['nome']
   search_fields = ['nome']


@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'descricao', 'genero', 'ano_lancamento', 'duracao']     
  search_fields = ['titulo', 'ano_lancamento']
  list_filter = ['ano_lancamento', 'genero']

admin.site.register(Token)
