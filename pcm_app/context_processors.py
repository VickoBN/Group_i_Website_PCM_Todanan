from .models import Profil, TautanTerkait


def pcm_global(request):
    return {
        'profil': Profil.objects.first(),
        'tautan_list': TautanTerkait.objects.all(),
    }