from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Berita


def berita_list(request):
    paginator = Paginator(Berita.objects.terbit(), 6)
    halaman = paginator.get_page(request.GET.get('page'))
    return render(request, 'pcm_app/berita_list.html', {'halaman': halaman})