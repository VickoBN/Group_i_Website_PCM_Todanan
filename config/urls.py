from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pcm_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# SEMENTARA: tampilkan 404.html buatan untuk semua alamat yang tidak ada.
# Harus paling bawah. Hapus sebelum commit.
def halaman_tidak_ditemukan(request, *args, **kwargs):
    return render(request, '404.html', status=404)


urlpatterns += [
    re_path(r'^.*$', halaman_tidak_ditemukan),
]