from django.db import models
from django.utils import timezone

class Agenda(models.Model):
    nama_kegiatan = models.CharField(max_length=200)
    waktu_mulai = models.DateTimeField()
    tempat = models.CharField(max_length=200, blank=True)
    keterangan = models.TextField(blank=True)

    class Meta:
        ordering = ['waktu_mulai']
        verbose_name_plural = 'Agenda'

    def __str__(self):
        return self.nama_kegiatan


class Dokumen(models.Model):
    judul = models.CharField(max_length=200)
    keterangan = models.TextField(blank=True)
    berkas = models.FileField(upload_to='dokumen/', blank=True)
    tautan_eksternal = models.URLField(blank=True, help_text='Isi jika dokumen berupa tautan.')
    tanggal_unggah = models.DateField(default=timezone.localdate)

    class Meta:
        ordering = ['-tanggal_unggah']
        verbose_name_plural = 'Dokumen'

    def __str__(self):
        return self.judul


class TautanTerkait(models.Model):
    nama = models.CharField(max_length=150)
    url = models.URLField()
    urutan = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['urutan', 'nama']
        verbose_name_plural = 'Tautan terkait'

    def __str__(self):
        return self.nama


class PesanMasuk(models.Model):
    nama = models.CharField(max_length=150)
    email = models.EmailField()
    subjek = models.CharField(max_length=200)
    pesan = models.TextField()
    waktu_kirim = models.DateTimeField(auto_now_add=True)
    sudah_dibaca = models.BooleanField(default=False)

    class Meta:
        ordering = ['-waktu_kirim']
        verbose_name_plural = 'Pesan masuk'

    def __str__(self):
        return f'{self.subjek} dari {self.nama}'