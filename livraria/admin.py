from django.contrib import admin

from livraria.models import Categoria, Editora, Autor, Livro

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)