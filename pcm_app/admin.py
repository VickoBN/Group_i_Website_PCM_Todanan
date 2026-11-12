from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Agenda, AmalUsaha, Berita, Dokumen, Pimpinan, Profil, Ranting, TautanTerkait, PesanMasuk,
)

admin.site.site_header = 'Admin PCM Todanan'
admin.site.site_title = 'Admin PCM Todanan'
admin.site.index_title = 'Kelola konten website'
admin.site.index_template = 'admin/pcm_index.html'


def _thumb(gambar):
    """Gambar kecil untuk kolom daftar/form admin."""
    if gambar:
        return format_html('<img src="{}" class="pcm-thumb" alt="">', gambar.url)
    return '—'


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nama_singkat', 'telepon', 'email')
    fieldsets = (
        ('Identitas', {'fields': ('nama', 'nama_singkat', 'tagline', 'gambar_hero')}),
        ('Tentang', {'fields': ('tentang', 'sejarah', 'visi', 'misi')}),
        ('Kontak', {'fields': ('alamat', 'telepon', 'email', 'jumlah_anggota_ktam')}),
    )

    def has_add_permission(self, request):
        return not Profil.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Pimpinan)
class PimpinanAdmin(admin.ModelAdmin):
    list_display = ('pratinjau', 'nama', 'jabatan', 'periode', 'urutan')
    list_display_links = ('nama',)
    list_editable = ('urutan',)
    search_fields = ('nama', 'jabatan')

    @admin.display(description='Foto')
    def pratinjau(self, obj):
        return _thumb(obj.foto)


@admin.register(Ranting)
class RantingAdmin(admin.ModelAdmin):
    list_display = ('nama', 'ketua', 'alamat', 'telepon')
    search_fields = ('nama', 'ketua')


@admin.register(AmalUsaha)
class AmalUsahaAdmin(admin.ModelAdmin):
    list_display = ('pratinjau', 'nama', 'bidang', 'alamat')
    list_display_links = ('nama',)
    list_filter = ('bidang',)
    search_fields = ('nama',)

    @admin.display(description='Gambar')
    def pratinjau(self, obj):
        return _thumb(obj.gambar)


@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('pratinjau', 'judul', 'status_label', 'tanggal_terbit')
    list_display_links = ('judul',)
    list_filter = ('status',)
    search_fields = ('judul', 'ringkasan')
    prepopulated_fields = {'slug': ('judul',)}
    date_hierarchy = 'tanggal_terbit'
    actions = ('terbitkan', 'jadikan_draf')

    @admin.display(description='Sampul')
    def pratinjau(self, obj):
        return _thumb(obj.gambar_sampul)

    @admin.display(description='Status', ordering='status')
    def status_label(self, obj):
        kelas = 'draf' if obj.status == Berita.Status.DRAF else ''
        return format_html('<span class="pcm-badge {}">{}</span>', kelas, obj.get_status_display())

    @admin.action(description='Terbitkan berita terpilih')
    def terbitkan(self, request, queryset):
        jumlah = queryset.update(status=Berita.Status.TERBIT)
        self.message_user(request, f'{jumlah} berita diterbitkan.')

    @admin.action(description='Jadikan draf')
    def jadikan_draf(self, request, queryset):
        jumlah = queryset.update(status=Berita.Status.DRAF)
        self.message_user(request, f'{jumlah} berita dijadikan draf.')


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nama_kegiatan', 'waktu_mulai', 'tempat')
    list_filter = ('waktu_mulai',)
    search_fields = ('nama_kegiatan', 'tempat')
    date_hierarchy = 'waktu_mulai'


@admin.register(Dokumen)
class DokumenAdmin(admin.ModelAdmin):
    list_display = ('judul', 'jenis', 'tanggal_unggah')
    search_fields = ('judul', 'keterangan')
    date_hierarchy = 'tanggal_unggah'

    @admin.display(description='Jenis')
    def jenis(self, obj):
        if obj.berkas:
            return 'Berkas'
        if obj.tautan_eksternal:
            return 'Tautan'
        return '—'


@admin.register(TautanTerkait)
class TautanTerkaitAdmin(admin.ModelAdmin):
    list_display = ('nama', 'url', 'urutan')
    list_editable = ('urutan',)


@admin.register(PesanMasuk)
class PesanMasukAdmin(admin.ModelAdmin):
    list_display = ('subjek', 'nama', 'email', 'waktu_kirim', 'status_baca')
    list_filter = ('sudah_dibaca', 'waktu_kirim')
    search_fields = ('nama', 'email', 'subjek')
    readonly_fields = ('nama', 'email', 'subjek', 'pesan', 'waktu_kirim')
    actions = ('tandai_dibaca', 'tandai_belum_dibaca')

    @admin.display(description='Status', ordering='sudah_dibaca')
    def status_baca(self, obj):
        if obj.sudah_dibaca:
            return format_html('<span class="pcm-badge">Dibaca</span>')
        return format_html('<span class="pcm-badge baru">Baru</span>')

    @admin.action(description='Tandai sudah dibaca')
    def tandai_dibaca(self, request, queryset):
        jumlah = queryset.update(sudah_dibaca=True)
        self.message_user(request, f'{jumlah} pesan ditandai sudah dibaca.')

    @admin.action(description='Tandai belum dibaca')
    def tandai_belum_dibaca(self, request, queryset):
        jumlah = queryset.update(sudah_dibaca=False)
        self.message_user(request, f'{jumlah} pesan ditandai belum dibaca.')

    def has_add_permission(self, request):
        return False