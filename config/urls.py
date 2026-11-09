from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path, re_path
import os
from django.urls import re_path
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pcm_app.urls')),
]


if not os.environ.get('AWS_STORAGE_BUCKET_NAME'):
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

# SEMENTARA: tampilkan 404.html buatan untuk semua alamat yang tidak ada.
# Harus paling bawah. Hapus sebelum commit.
def halaman_tidak_ditemukan(request, *args, **kwargs):
    return render(request, '404.html', status=404)


urlpatterns += [
    re_path(r'^.*$', halaman_tidak_ditemukan),
]