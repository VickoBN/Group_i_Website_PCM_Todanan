from django.core.management.base import BaseCommand

from pcm_app.models import Pimpinan, Profil, Ranting

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


class Command(BaseCommand):
    help = 'Mengisi data riil PCM Todanan.'

    def handle(self, *args, **options):
        self.isi_profil()
        self.isi_pimpinan()
        self.isi_ranting()
        self.stdout.write(self.style.SUCCESS('Data PCM Todanan berhasil diisi.'))

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