from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Agenda, Berita
from .models import Berita, Dokumen
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PesanForm

def kontak(request):
    if request.method == 'POST':
        form = PesanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Terima kasih, pesan Anda sudah terkirim.')
            return redirect('pcm_app:kontak')
    else:
        form = PesanForm()
    return render(request, 'pcm_app/kontak.html', {'form': form})

def berita_list(request):
    paginator = Paginator(Berita.objects.terbit(), 6)
    halaman = paginator.get_page(request.GET.get('page'))
    return render(request, 'pcm_app/berita.html', {
        'halaman': halaman,
        'daftar': halaman,
    })

def berita_detail(request, slug):
    berita = get_object_or_404(Berita.objects.terbit(), slug=slug)
    lainnya = Berita.objects.terbit().exclude(pk=berita.pk)[:3]
    return render(request, 'pcm_app/berita.html', {
        'berita': berita,
        'daftar': lainnya,
    })

def agenda(request):
    sekarang = timezone.now()
    konteks = {
        'akan_datang': Agenda.objects.filter(waktu_mulai__gte=sekarang),
        'terlaksana': Agenda.objects.filter(waktu_mulai__lt=sekarang).order_by('-waktu_mulai'),
    }
    return render(request, 'pcm_app/agenda.html', konteks)

def unduhan(request):
    return render(request, 'pcm_app/unduhan.html', {'daftar_dokumen': Dokumen.objects.all()})