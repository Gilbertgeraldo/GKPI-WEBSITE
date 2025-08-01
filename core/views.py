from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import jemaat, Berita, Galeri, Struktural

def index(request):
    return render(request, 'core/index.html')

def daftar_berita(request):
    semua_berita = Berita.objects.all().order_by('-created_at')
    context = {
        'page_title': 'Warta Jemaat',
        'daftar_berita': semua_berita
    }
    return render(request, 'core/berita_list.html',context)

def detail_berita(request,berita_id):
    berita = get_object_or_404(Berita, pk=berita_id)
    context = {
        'page_title': 'Detail Berita',
        'daftar_berita': berita,
    }
    return render(request, 'core/list.html',context)

def jemaat_list(request):
    jemaat_list = jemaat.objects.all()
    return render(request, 'core/jemaat_list.html', {'galeri_foto':jemaat_list})

def galeri_foto(request):
    galeri_list = Galeri.objects.all()
    return render(request, 'core/foto.html', {'galeri_foto': galeri_list})

def struktural_gereja(request):
    struktural_list = Struktural.objects.all()
    return render(request, 'core/struktural.html'), {'struktural': struktural_list}

def livestream(request):
    return render(request, 'core/livestream.html')

def register_view(request):
    return render(request, 'core/register.html')

def login_view(request):
    return render(request, 'core/login.html')

def logout_view(request):
    return redirect('index')

@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html')

@login_required
def struktural_admin_list(request):
    struktural_list = Struktural.objects.all()
    return render(request, 'core/list.html', {'struktural': struktural_list})