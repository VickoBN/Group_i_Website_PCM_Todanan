from django.shortcuts import render
from django.utils import timezone

from .models import Agenda, AmalUsaha, Berita, Ranting


def beranda(request):
    konteks = {
        'jumlah_ranting': Ranting.objects.count(),
        'jumlah_amal_usaha': AmalUsaha.objects.count(),
        'berita_terbaru': Berita.objects.terbit()[:3],
        'agenda_mendatang': Agenda.objects.filter(
            waktu_mulai__gte=timezone.now()
        )[:3],
    }
    return render(request, 'pcm_app/beranda.html', konteks)