# File: core/admin.py
# Deskripsi: Mendaftarkan model ke Django Admin Panel.

from django.contrib import admin
from .models import Berita, Galeri, Struktural

# Daftarkan model Anda di sini agar muncul di halaman admin.

@admin.register(Berita)
class BeritaAdmin(admin.ModelAdmin):
    list_display = ('judul', 'penulis', 'created_at')
    list_filter = ('created_at', 'penulis')
    search_fields = ('judul', 'isi')

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):
    list_display = ('judul', 'diunggah_oleh', 'uploaded_at')

@admin.register(Struktural)
class StrukturalAdmin(admin.ModelAdmin):
    list_display = ('nama_lengkap', 'jabatan', 'periode', 'urutan')
