from django.shortcuts import render
from django.views.generic import TemplateView
import requests


class PaginaLivros(TemplateView):
    template_name = 'livros.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url_livros = 'http://127.0.0.1:8001/api/v1/books/'
        headers = {"Authorization": "Token 272eadc957d31c823cb857239a70e53961393436"}
        response = requests.get(url=url_livros, headers=headers)
        
        if response.status_code == 200:
            livros = response.json()
        else:
            livros = []
        
        context['livros'] = livros
        return context