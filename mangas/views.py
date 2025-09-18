from django.shortcuts import render
from .models import Manga

def liste_mangas(request):
    mangas = Manga.objects.all()
    return render(request, 'mangas/liste.html', {'mangas': mangas})