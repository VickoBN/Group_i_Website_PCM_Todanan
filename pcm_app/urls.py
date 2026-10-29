from django.urls import path

from . import placeholder

# Orang 3: ganti baris komentar ini dengan: from . import views

from . import views_konten

app_name = 'pcm_app'

urlpatterns = [
    path('', placeholder.sementara, name='beranda'),
    path('profil/', placeholder.sementara, name='profil'),
    path('pimpinan/', placeholder.sementara, name='pimpinan'),
    path('ranting/', placeholder.sementara, name='ranting'),
    path('amal-usaha/', placeholder.sementara, name='amal_usaha'),

    path('berita/', placeholder.sementara, name='berita_list'),
    path('berita/', views_konten.berita_list, name='berita_list'),
    path('berita/<slug:slug>/', placeholder.sementara, name='berita_detail'),
    path('agenda/', placeholder.sementara, name='agenda'),
    path('unduhan/', placeholder.sementara, name='unduhan'),
    path('kontak/', placeholder.sementara, name='kontak'),
]