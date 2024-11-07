from django.urls import path
from .views import PaginaLivros

urlpatterns = [
    path('', PaginaLivros.as_view(), name='homepage_books'),
]