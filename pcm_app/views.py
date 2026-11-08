from django.shortcuts import render
from django.utils import timezone

from .models import Agenda, AmalUsaha, Berita, Pimpinan, Profil, Ranting


def beranda(request):
    profil_data = Profil.objects.first()
    konteks = {
        'profil': profil_data,
        'jumlah_ranting': Ranting.objects.count(),
        'jumlah_amal_usaha': AmalUsaha.objects.count(),
        'berita_terbaru': Berita.objects.terbit()[:3] if hasattr(Berita.objects, 'terbit') else Berita.objects.all()[:3],
        'agenda_mendatang': Agenda.objects.filter(waktu_mulai__gte=timezone.now())[:3],
    }
    return render(request, 'pcm_app/beranda.html', konteks)


def halaman_profil(request):
    profil_data = Profil.objects.first()
    return render(request, 'pcm_app/profil.html', {'profil': profil_data})


def halaman_pimpinan(request):
    return render(request, 'pcm_app/pimpinan.html', {'daftar_pimpinan': Pimpinan.objects.all()})


def ranting(request):
    return render(request, 'pcm_app/ranting.html', {'daftar_ranting': Ranting.objects.all()})


def amal_usaha(request):
    return render(request, 'pcm_app/amal_usaha.html', {'daftar_amal_usaha': AmalUsaha.objects.all()})