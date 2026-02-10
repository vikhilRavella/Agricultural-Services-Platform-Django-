from pathlib import Path
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# ================= BASE =================
BASE_DIR = Path(__file__).resolve().parent.parent

# ================= DEMO MODE =================
# settings.py

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ❌ REMOVE any DEMO_MODE_ENABLED logic

ALLOWED_HOSTS = [
    'agricultural-services-platform-django.onrender.com',
]

# ================= SECURITY =================
SECRET_KEY = "django-insecure-h+$3%dwi3p$my#%io*16$yq5saja%$*u=4gq89)x6_u-2@m203"
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# ================= APPLICATIONS =================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',

    # Local apps
    'accounts',
    'services',
    'suppliers',
    'dashboard',
]

# ================= MIDDLEWARE =================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# ================= URLS & TEMPLATES =================
ROOT_URLCONF = 'agro_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'dashboard.context_processors.demo_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'agro_platform.wsgi.application'

# ================= DATABASE =================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ================= AUTH =================
AUTH_USER_MODEL = 'accounts.User'

# ================= PASSWORD VALIDATION =================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================= I18N =================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ================= STATIC & MEDIA =================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ================= DEFAULT PK =================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

