from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6ehjgj$9f98a053kx5m3w%3mn@-_+m78*tz=hx_rpt1ujqu(vr'

DEBUG = True

ALLOWED_HOSTS = []

# Aplikasi
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # App kamu
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gkpionline.urls'

# 🔧 TEMPLATE SETTING
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Tambahkan direktori global template jika kamu ingin menaruh file HTML di luar app
        'DIRS': [],
        'APP_DIRS': True,  # Penting agar Django mencari templates dalam folder app/templates/
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # <-- tambahkan ini
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gkpionline.wsgi.application'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# PASSWORD VALIDATOR
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# LOCALE
LANGUAGE_CODE = 'id'  # ubah ke bahasa Indonesia jika diinginkan
TIME_ZONE = 'Asia/Jakarta'  # ubah sesuai lokasi kamu

USE_I18N = True
USE_TZ = True

# 🔧 STATIC FILES (CSS, JS, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),  # atau 'static' jika foldernya di root
]

# Untuk deploy nanti
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Primary Key Default
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
