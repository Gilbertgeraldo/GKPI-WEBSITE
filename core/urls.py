from django.urls import path
from . import views

urlpatterns = [
    path('beranda', views.index, name='index'),
    path('berita/', views.daftar_berita, name='daftar-berita'),
    path('berita/<int:berita_id>/', views.detail_berita, name='detail-berita'),
    path('galeri/', views.galeri_foto, name='galeri'),
    path('struktural/', views.struktural_gereja, name='struktural'),
    path('livestream/', views.livestream, name='livestream'),

    # URL untuk otentikasi (login, register, logout)
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # URL untuk halaman setelah login
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
