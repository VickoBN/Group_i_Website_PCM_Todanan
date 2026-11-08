from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Berita, PesanMasuk, Profil


class HalamanPublikTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Profil.objects.create(nama='PCM Todanan', nama_singkat='PCM Todanan')
        cls.terbit = Berita.objects.create(
            judul='Berita Terbit', ringkasan='ringkasan', isi='isi berita',
            status=Berita.Status.TERBIT,
        )
        cls.draf = Berita.objects.create(
            judul='Berita Draf', ringkasan='ringkasan', isi='isi berita',
            status=Berita.Status.DRAF,
        )
        cls.masa_depan = Berita.objects.create(
            judul='Berita Masa Depan', ringkasan='ringkasan', isi='isi berita',
            status=Berita.Status.TERBIT,
            tanggal_terbit=timezone.now() + timedelta(days=3),
        )

    def test_semua_halaman_publik_200(self):
        nama_url = [
            'beranda', 'profil', 'pimpinan', 'ranting', 'amal_usaha',
            'berita_list', 'agenda', 'unduhan', 'kontak',
        ]
        for nama in nama_url:
            with self.subTest(nama=nama):
                respons = self.client.get(reverse('pcm_app:' + nama))
                self.assertEqual(respons.status_code, 200)

    def test_detail_berita_terbit_200(self):
        url = reverse('pcm_app:berita_detail', args=[self.terbit.slug])
        self.assertEqual(self.client.get(url).status_code, 200)

    def test_berita_draf_404(self):
        url = reverse('pcm_app:berita_detail', args=[self.draf.slug])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_berita_masa_depan_404(self):
        url = reverse('pcm_app:berita_detail', args=[self.masa_depan.slug])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_daftar_berita_hanya_yang_terbit(self):
        respons = self.client.get(reverse('pcm_app:berita_list'))
        self.assertContains(respons, 'Berita Terbit')
        self.assertNotContains(respons, 'Berita Draf')
        self.assertNotContains(respons, 'Berita Masa Depan')

    def test_slug_tetap_unik_untuk_judul_sama(self):
        kembar = Berita.objects.create(judul='Berita Terbit', ringkasan='r', isi='i')
        self.assertNotEqual(kembar.slug, self.terbit.slug)

    def test_formulir_kontak_menyimpan_pesan(self):
        data = {
            'nama': 'Budi', 'email': 'budi@example.com', 'subjek': 'Tanya',
            'pesan': 'Halo, saya ingin bertanya tentang kegiatan.',
        }
        respons = self.client.post(reverse('pcm_app:kontak'), data)
        self.assertRedirects(respons, reverse('pcm_app:kontak'))
        self.assertEqual(PesanMasuk.objects.count(), 1)

    def test_formulir_kontak_menolak_pesan_pendek(self):
        data = {'nama': 'Budi', 'email': 'budi@example.com', 'subjek': 'Tanya', 'pesan': 'Halo'}
        respons = self.client.post(reverse('pcm_app:kontak'), data)
        self.assertEqual(respons.status_code, 200)
        self.assertEqual(PesanMasuk.objects.count(), 0)