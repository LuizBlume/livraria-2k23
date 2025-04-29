from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrive":
            return LivroDetailSerializer
        return LivroSerializer