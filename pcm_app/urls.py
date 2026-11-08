from django.urls import path
from . import views
from . import view_konten

app_name = 'pcm_app'

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('profil/', views.halaman_profil, name='profil'),
    path('pimpinan/', views.halaman_pimpinan, name='pimpinan'),
    path('ranting/', views.ranting, name='ranting'),
    path('amal-usaha/', views.amal_usaha, name='amal_usaha'),

    path('berita/', view_konten.berita_list, name='berita_list'),
    path('berita/<slug:slug>/', view_konten.berita_detail, name='berita_detail'),

    path('unduhan/', view_konten.unduhan, name='unduhan'),
    path('kontak/', view_konten.kontak, name='kontak'),
    path('agenda/', view_konten.agenda, name='agenda'),
]