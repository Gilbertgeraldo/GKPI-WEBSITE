from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('berita/', views.daftar_berita, name='daftar_berita'),
    path('berita/<int:berita_id>/', views.detail_berita, name='detail_berita'),
    path('galeri/', views.galeri_foto, name='galeri_foto'),
    path('struktur/', views.struktural_gereja, name='struktur'),
    path('livestream/', views.livestream, name='livestream'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]

