from django import template
from django.utils import timezone

from pcm_app.models import Agenda, AmalUsaha, Berita, Dokumen, PesanMasuk, Ranting

register = template.Library()


@register.simple_tag
def pcm_statistik():
    """Angka ringkas untuk dasbor admin."""
    return {
        'berita_terbit': Berita.objects.terbit().count(),
        'berita_draf': Berita.objects.filter(status=Berita.Status.DRAF).count(),
        'agenda_mendatang': Agenda.objects.filter(waktu_mulai__gte=timezone.now()).count(),
        'pesan_baru': PesanMasuk.objects.filter(sudah_dibaca=False).count(),
        'ranting': Ranting.objects.count(),
        'amal_usaha': AmalUsaha.objects.count(),
        'dokumen': Dokumen.objects.count(),
    }