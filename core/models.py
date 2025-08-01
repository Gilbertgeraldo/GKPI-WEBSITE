# File: core/models.py
# Deskripsi: Mendefinisikan semua tabel database untuk aplikasi gereja.

from django.db import models
from django.contrib.auth.models import User # Menggunakan User bawaan Django

class jemaat(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    alamat = models.TextField()
    
class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    # 'upload_to' akan membuat subfolder di dalam folder media Anda
    gambar = models.ImageField(upload_to='berita_images/', blank=True, null=True)
    penulis = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name_plural = "Berita" # Nama yang lebih baik di admin panel

class Galeri(models.Model):
    judul = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='galeri_images/')
    keterangan = models.TextField(blank=True)
    diunggah_oleh = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = "Galeri"

class Struktural(models.Model):
    nama_lengkap = models.CharField(max_length=150)
    jabatan = models.CharField(max_length=100)
    foto_profil = models.ImageField(upload_to='struktural_images/', blank=True, null=True)
    periode = models.CharField(max_length=50, help_text="Contoh: 2024-2029")
    urutan = models.PositiveIntegerField(default=0, help_text="Untuk pengurutan tampilan")

    class Meta:
        ordering = ['urutan']
        verbose_name_plural = "Struktural"

    def __str__(self):
        return f"{self.nama_lengkap} - {self.jabatan}"

from django.db import models
from django.contrib.auth.models import User # Menggunakan User bawaan Django

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    # 'upload_to' akan membuat subfolder di dalam folder media Anda
    gambar = models.ImageField(upload_to='berita_images/', blank=True, null=True)
    penulis = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name_plural = "Berita" # Nama yang lebih baik di admin panel

class Galeri(models.Model):
    judul = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='galeri_images/')
    keterangan = models.TextField(blank=True)
    diunggah_oleh = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = "Galeri"

class Struktural(models.Model):
    nama_lengkap = models.CharField(max_length=150)
    jabatan = models.CharField(max_length=100)
    foto_profil = models.ImageField(upload_to='struktural_images/', blank=True, null=True)
    periode = models.CharField(max_length=50, help_text="Contoh: 2024-2029")
    urutan = models.PositiveIntegerField(default=0, help_text="Untuk pengurutan tampilan")

    class Meta:
        ordering = ['urutan']
        verbose_name_plural = "Struktural"

    def __str__(self):
        return f"{self.nama_lengkap} - {self.jabatan}"
