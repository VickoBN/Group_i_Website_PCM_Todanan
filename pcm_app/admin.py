from django.contrib import admin

from .models import AmalUsaha, Pimpinan, Profil, Ranting

admin.site.site_header = 'Admin Website PCM Todanan'
admin.site.site_title = 'Admin PCM Todanan'
admin.site.index_title = 'Kelola konten website'


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
   list_display = ('nama', 'nama_singkat', 'telepon', 'email')

   def has_add_permission(self, request):
       return not Profil.objects.exists()

   def has_delete_permission(self, request, obj=None):
       return False


@admin.register(Pimpinan)
class PimpinanAdmin(admin.ModelAdmin):
   list_display = ('nama', 'jabatan', 'periode', 'urutan')
   list_editable = ('urutan',)
   search_fields = ('nama', 'jabatan')


@admin.register(Ranting)
class RantingAdmin(admin.ModelAdmin):
   list_display = ('nama', 'ketua', 'alamat')
   search_fields = ('nama', 'ketua')


@admin.register(AmalUsaha)
class AmalUsahaAdmin(admin.ModelAdmin):
   list_display = ('nama', 'bidang', 'alamat')
   list_filter = ('bidang',)
   search_fields = ('nama',)