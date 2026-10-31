from django.shortcuts import render
from .models import Agenda, AmalUsaha, Berita, Pimpinan, Ranting

def halaman_profil(request):
    return render(request, 'pcm_app/profil.html')

def halaman_pimpinan(request):
    return render(request, 'pcm_app/pimpinan.html', {'daftar_pimpinan': Pimpinan.objects.all()})