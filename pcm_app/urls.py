from django.urls import path

from . import placeholder

from . import views

# Orang 4: ganti baris komentar ini dengan: from . import views_konten

app_name = 'pcm_app'

urlpatterns = [
    # --- Bagian Orang 3 ---
    path('', placeholder.sementara, name='beranda'),
    path('profil/', views.halaman_profil, name='profil'),
    path('pimpinan/', placeholder.sementara, name='pimpinan'),
    path('ranting/', placeholder.sementara, name='ranting'),
    path('amal-usaha/', placeholder.sementara, name='amal_usaha'),

    # --- Bagian Orang 4 ---
    path('berita/', placeholder.sementara, name='berita_list'),
    path('berita/<slug:slug>/', placeholder.sementara, name='berita_detail'),
    path('agenda/', placeholder.sementara, name='agenda'),
    path('unduhan/', placeholder.sementara, name='unduhan'),
    path('kontak/', placeholder.sementara, name='kontak'),
]