from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
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
    return render(request, 'pcm_app/pimpinan.html', {
        'profil': Profil.objects.first(),
        'pimpinan': Pimpinan.objects.all(),
    })


def ranting(request):
    return render(request, 'pcm_app/ranting.html', {
        'profil': Profil.objects.first(),
        'ranting': Ranting.objects.all(),
    })


def amal_usaha(request):
    return render(request, 'pcm_app/amal_usaha.html', {
        'profil': Profil.objects.first(),
        'amal_usaha': AmalUsaha.objects.all(),
    })


def berita_list(request):
    paginator = Paginator(Berita.objects.terbit(), 9)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'pcm_app/berita_list.html', {
        'profil': Profil.objects.first(),
        'page_obj': page_obj,
    })


def berita_detail(request, slug):
    berita = get_object_or_404(Berita.objects.terbit(), slug=slug)
    lainnya = Berita.objects.terbit().exclude(pk=berita.pk)[:3]
    return render(request, 'pcm_app/berita_detail.html', {
        'profil': Profil.objects.first(),
        'berita': berita,
        'lainnya': lainnya,
    })