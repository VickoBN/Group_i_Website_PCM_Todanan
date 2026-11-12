from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from pcm_app.models import (
    Agenda, Berita, Dokumen, Pimpinan, Profil, Ranting, TautanTerkait,
)
# Semua data berasal dari README repo ini (formulir Google Forms pengurus PCM,
# diambil 28 Oktober 2026). Jangan menambah data karangan.

PROFIL = {
    'nama': 'Pimpinan Cabang Muhammadiyah Todanan',
    'nama_singkat': 'PCM Todanan',
    'tagline': 'Islam Berkemajuan',
    'tentang': 'Gerakan dakwah amar ma’ruf nahi munkar dan tajdid sesuai Al-Qur’an dan As-Sunnah.',
    'sejarah': 'Berdiri sekitar akhir tahun 1968 sampai awal tahun 1970-an oleh keluarga pendiri Mbah Muhtarom.',
    'visi': 'Menegakkan dan menjunjung tinggi agama Islam dan bertekad untuk mewujudkan masyarakat Islam yang sebenar-benarnya.',
    'misi': '',  # README belum memuat misi khusus PCM; dikosongkan
    'alamat': 'Jl. Raya Pule-Todanan, Kec. Todanan, Kab. Blora',
    'telepon': '082325132159',
    'email': 'pcmtodanan@gmail.com',
    'jumlah_anggota_ktam': 150,  # README: kurang lebih 150 orang
}

KETUA = {
    'nama': 'Wahyu Dwi Atmodjo, S.T',
    'jabatan': 'Ketua',
    'periode': '2023–2028',
    'urutan': 1,
}

RANTING = [
    ('PRM Todanan', 'Nurhadi Purnomo, S.Pd.I', 'Dukuh Bulumanis, Kec. Todanan'),
    ('PRM Jomblang', 'Abdullah', 'Dukuh Jomblang, Kec. Todanan'),
    ('PRM Dalangan', 'Wakijo', 'Desa Dalangan'),
    ('PRM Pelemsengir', 'Jauhar Arifin, S.Pd.I', 'Desa Pelemsengir'),
    ('PRM Ketileng', 'Sudiono, M.Si', 'Dukuh Patihan, Desa Ketileng'),
    ('PRM Bedingin', 'Gumeg Supardi', 'Desa Banat, Desa Bedingin'),
    ('PRM Kedungwungu', 'Susanto, S.Pd', 'Desa Kedungwungu'),
    ('PRM Tinapan', 'Didik Suprianto', 'Desa Tinapan'),
]
DOKUMEN = [
    ('Panduan Muscab Muhammadiyah ’Aisyiyah 2023',
     'Buku panduan pelaksanaan Musyawarah Cabang Muhammadiyah dan ’Aisyiyah Todanan 2023, memuat LPJ aset tanah SIMAM, majelis, dan susunan pengurus lengkap. Terbit 22 Juli 2023.',
     'https://share.google/H3oaAJo2XqwGgpnFX'),
    ('Surat Permohonan Dana OK',
     'Surat resmi permohonan bantuan dana kegiatan Musyawarah Cabang kepada PCM Todanan dan LAZISMU Todanan. Desember 2024.',
     'https://share.google/QQcPi2JuIIVi9vSU6'),
    ('SK PCNA Todanan',
     'Surat Keputusan PDNA Kabupaten Blora tentang pengesahan pengurus PC Nasyiatul Aisyiyah Todanan periode 2022–2026. Maret 2025.',
     'https://share.google/PwX2qdPmCXCEznTWy'),
]

# Judul asli belum diketahui; ganti lewat admin setelah membuka tiap tautan.
BERITA = [
    ('berita-pcm-todanan-1', 'Berita PCM Todanan 1', 'https://share.google/hXuU3HCn0XRZ3SB94', 'YYYY-MM-DD'),
    ('berita-pcm-todanan-2', 'Berita PCM Todanan 2', 'https://share.google/c1QuOGOxoxBIhVfET', 'YYYY-MM-DD'),
    ('berita-pcm-todanan-3', 'Berita PCM Todanan 3', 'https://share.google/I6gmrIF9xOjuio3EW', 'YYYY-MM-DD'),
]

TAUTAN = [
    ('PP Muhammadiyah', 'https://muhammadiyah.or.id', 1),
    # WAJIB ditambah: situs resmi PDM Kabupaten Blora dan PWM Jawa Tengah.
    # Cari URL-nya, buka satu per satu sampai terbukti bisa diakses, baru tambahkan.
]

class Command(BaseCommand):
    help = 'Mengisi data riil PCM Todanan.'

    def handle(self, *args, **options):
        self.isi_profil()
        self.isi_pimpinan()
        self.isi_ranting()
        self.isi_dokumen()
        self.isi_agenda()
        self.isi_berita()
        self.isi_tautan()
        self.stdout.write(self.style.SUCCESS('Data PCM Todanan berhasil diisi.'))

    def isi_dokumen(self):
        for judul, keterangan, url in DOKUMEN:
            Dokumen.objects.get_or_create(
                judul=judul,
                defaults={'keterangan': keterangan, 'tautan_eksternal': url},
            )

    def isi_agenda(self):
        # README hanya menyebut tanggalnya; jam belum diketahui (tampilan hanya tanggal).
        Agenda.objects.get_or_create(
            nama_kegiatan='Milad Muhammadiyah',
            defaults={
                'waktu_mulai': timezone.make_aware(datetime(2026, 11, 18)),
                'tempat': 'SMK Muhammadiyah',
            },
        )

    def isi_berita(self):
        for slug, judul, url, tanggal in BERITA:
            Berita.objects.get_or_create(
                slug=slug,
                defaults={
                    'judul': judul,
                    'ringkasan': 'Pemberitaan tentang PCM Todanan. Baca selengkapnya di sumber asli.',
                    'isi': 'Pemberitaan tentang PCM Todanan dari media online. Baca selengkapnya di sumber asli melalui tautan di bawah.',
                    'sumber_url': url,
                    'tanggal_terbit': timezone.make_aware(
                        datetime.strptime(tanggal, '%Y-%m-%d')
                    ),
                    'status': Berita.Status.TERBIT,
                },
        )

    def isi_tautan(self):
        for nama, url, urutan in TAUTAN:
            TautanTerkait.objects.get_or_create(
                nama=nama, defaults={'url': url, 'urutan': urutan},
            )
    def isi_profil(self):
        profil = Profil.objects.first() or Profil()
        for kolom, nilai in PROFIL.items():
            setattr(profil, kolom, nilai)
        profil.save()

    def isi_pimpinan(self):
        Pimpinan.objects.update_or_create(jabatan=KETUA['jabatan'], defaults=KETUA)

    def isi_ranting(self):
        for nama, ketua, alamat in RANTING:
            Ranting.objects.update_or_create(
                nama=nama, defaults={'ketua': ketua, 'alamat': alamat},
            )