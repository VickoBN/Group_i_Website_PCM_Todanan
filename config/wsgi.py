"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Pengecekan sementara storage dan URL foto
from django.core.files.storage import default_storage
from pcm_app.models import Pimpinan

print("=== CEK STORAGE PCM TODANAN ===")
print("Storage aktif:", default_storage.__class__.__name__)

try:
    p = Pimpinan.objects.first()
    if p and p.foto:
        print("Nama foto:", p.foto.name)
        print("URL foto:", p.foto.url)
    else:
        print("Data pimpinan atau foto tidak ditemukan.")
except Exception as e:
    print("Gagal mengecek foto:", type(e).__name__)

print("=== SELESAI CEK STORAGE ===")
