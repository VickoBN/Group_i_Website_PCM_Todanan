from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Profil(models.Model):
    nama = models.CharField(max_length=200)
    nama_singkat = models.CharField(max_length=50)
    tagline = models.CharField(max_length=200, blank=True)
    tentang = models.TextField(blank=True)
    sejarah = models.TextField(blank=True)
    visi = models.TextField(blank=True)
    misi = models.TextField(blank=True, help_text='Satu misi per baris.')
    alamat = models.CharField(max_length=255, blank=True)
    telepon = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    jumlah_anggota_ktam = models.PositiveIntegerField(default=0)
    gambar_hero = models.ImageField(upload_to='hero/', blank=True)

    class Meta:
        verbose_name = 'Profil organisasi'
        verbose_name_plural = 'Profil organisasi'

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        if not self.pk and Profil.objects.exists():
            raise ValidationError('Profil organisasi hanya boleh satu baris.')
        super().save(*args, **kwargs)

    @property
    def daftar_misi(self):
        return [baris.strip() for baris in self.misi.splitlines() if baris.strip()]


class Pimpinan(models.Model):
    nama = models.CharField(max_length=150)
    jabatan = models.CharField(max_length=100)
    periode = models.CharField(max_length=20, help_text='Contoh: 2023–2028')
    foto = models.ImageField(upload_to='pimpinan/', blank=True)
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['urutan', 'nama']
        verbose_name_plural = 'Pimpinan'

    def __str__(self):
        return f'{self.nama} ({self.jabatan})'