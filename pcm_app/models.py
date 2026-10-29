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



class Ranting(models.Model):
    nama = models.CharField(max_length=100)
    ketua = models.CharField(max_length=150, blank=True)
    alamat = models.CharField(max_length=255, blank=True)
    telepon = models.CharField(max_length=30, blank=True, help_text='Hanya kontak resmi.')

    class Meta:
        ordering = ['nama']

    def __str__(self):
        return self.nama


class AmalUsaha(models.Model):
    class Bidang(models.TextChoices):
        PENDIDIKAN = 'pendidikan', 'Pendidikan'
        KESEHATAN = 'kesehatan', 'Kesehatan'
        SOSIAL = 'sosial', 'Sosial'
        EKONOMI = 'ekonomi', 'Ekonomi'

    nama = models.CharField(max_length=200)
    bidang = models.CharField(max_length=20, choices=Bidang.choices)
    deskripsi = models.TextField(blank=True)
    alamat = models.CharField(max_length=255, blank=True)
    gambar = models.ImageField(upload_to='amal-usaha/', blank=True)

    class Meta:
        ordering = ['bidang', 'nama']
        verbose_name_plural = 'Amal usaha'

    def __str__(self):
        return self.nama


class BeritaQuerySet(models.QuerySet):
    def terbit(self):
        return self.filter(
            status=Berita.Status.TERBIT,
            tanggal_terbit__lte=timezone.now(),
        )


class Berita(models.Model):
    class Status(models.TextChoices):
        DRAF = 'draf', 'Draf'
        TERBIT = 'terbit', 'Terbit'

    judul = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    ringkasan = models.CharField(max_length=300)
    isi = models.TextField()
    gambar_sampul = models.ImageField(upload_to='berita/', blank=True)
    sumber_url = models.URLField(blank=True, help_text='Tautan berita asli, jika ada.')
    tanggal_terbit = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAF)

    objects = BeritaQuerySet.as_manager()

    class Meta:
        ordering = ['-tanggal_terbit']
        verbose_name_plural = 'Berita'

    def __str__(self):
        return self.judul

    def save(self, *args, **kwargs):
        if not self.slug:
            dasar = slugify(self.judul)[:200] or 'berita'
            slug, nomor = dasar, 2
            while Berita.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{dasar}-{nomor}'
                nomor += 1
            self.slug = slug
        super().save(*args, **kwargs)    