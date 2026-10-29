from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Berita


def berita_list(request):
    paginator = Paginator(Berita.objects.terbit(), 6)
    halaman = paginator.get_page(request.GET.get('page'))
    return render(request, 'pcm_app/berita_list.html', {'halaman': halaman})

def berita_detail(request, slug):
    berita = get_object_or_404(Berita.objects.terbit(), slug=slug)
    lainnya = Berita.objects.terbit().exclude(pk=berita.pk)[:3]
    return render(request, 'pcm_app/berita_detail.html', {'berita': berita, 'lainnya': lainnya})