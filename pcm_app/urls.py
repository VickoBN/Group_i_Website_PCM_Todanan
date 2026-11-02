from django.urls import path

from . import placeholder

from . import views

from . import views_konten

app_name = 'pcm_app'

urlpatterns = [
    path('', placeholder.sementara, name='beranda'),
    path('profil/', views.halaman_profil, name='profil'),
    path('pimpinan/', views.halaman_pimpinan, name='pimpinan'),
    path('ranting/', placeholder.sementara, name='ranting'),
    path('amal-usaha/', placeholder.sementara, name='amal_usaha'),

    path('berita/', placeholder.sementara, name='berita_list'),
    path('berita/', views_konten.berita_list, name='berita_list'),
    path('berita/<slug:slug>/', views_konten.berita_detail, name='berita_detail'),
    path('berita/<slug:slug>/', placeholder.sementara, name='berita_detail'),
    
    path('unduhan/', placeholder.sementara, name='unduhan'),
    path('unduhan/', views_konten.unduhan, name='unduhan'),
    
    path('kontak/', placeholder.sementara, name='kontak'),
    
    path('agenda/', placeholder.sementara, name='agenda'),
    path('agenda/', views_konten.agenda, name='agenda')
]