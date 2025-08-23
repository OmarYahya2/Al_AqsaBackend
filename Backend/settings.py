from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-)zff25@-fnl(8*k2d&=4%xemu6!uexm_9_%9r&h1_qq@(n6fud')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'  # تفعيل DEBUG مؤقتاً

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'al-aqsabackend-1-pv0k.onrender.com,al-aqsabackend-uokt.onrender.com,localhost,127.0.0.1').split(',')

# إضافة الدومين الذي تولده Render تلقائياً
render_host = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if render_host:
    ALLOWED_HOSTS.append(render_host)

# للتطوير - السماح لجميع المضيفين إذا كان DEBUG=True
if DEBUG:
    ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Backend.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# إعدادات قاعدة البيانات
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # استخدام DATABASE_URL إذا كان متوفراً
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    # إعدادات PostgreSQL يدوية
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'mydb_5kr4'),
            'USER': os.environ.get('DB_USER', 'mydb_5kr4_user'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'SFDQSlNoYjRPpsC9hbHiK4PQBKEI6w3H'),
            'HOST': os.environ.get('DB_HOST', 'dpg-d2krgrjipnbc73fgg7n0-a.oregon-postgres.render.com'),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {
                'sslmode': 'require',
            }
        }
    }




# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'ar'

TIME_ZONE = 'Asia/Gaza'

USE_I18N = True

USE_TZ = True

# إعدادات اللغة
LANGUAGES = [
    ('ar', 'العربية'),
    ('en', 'English'),
]

# إعدادات التاريخ والوقت
USE_L10N = True
DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'Y-m-d H:i'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Static files collection for deployment
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# WhiteNoise settings for serving static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# WhiteNoise configuration
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = True
WHITENOISE_SKIP_COMPRESS_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'zip', 'gz', 'tgz', 'bz2', 'tbz', 'xz', 'br']

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "https://al-aqsamedical-lab.vercel.app",  # frontend vercel الجديد
    "https://al-aqsa-medical-lab.vercel.app",  # frontend vercel القديم
    "http://localhost:3000",  # للتجربة من الجهاز المحلي
]

# Additional CORS settings
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOWED_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# CSRF Settings for API
CSRF_TRUSTED_ORIGINS = [
    "https://al-aqsamedical-lab.vercel.app",  # frontend vercel الجديد
    "https://al-aqsa-medical-lab.vercel.app",  # frontend vercel القديم
    "https://al-aqsabackend-1-pv0k.onrender.com",  # backend الجديد
    "https://al-aqsabackend-uokt.onrender.com",  # backend القديم
]

# إضافة CSRF trusted origins للدومين الذي تولده Render
if render_host:
    CSRF_TRUSTED_ORIGINS.append(f"https://{render_host}")

# إعدادات إضافية للإنتاج
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_TZ = True

# إعدادات logging للإنتاج
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# إعدادات Django Admin
ADMIN_URL = 'admin/'

# تحسين أداء Admin
ADMIN_MEDIA_PREFIX = '/static/admin/'

# إعدادات إضافية للـ Admin في الإنتاج
if not DEBUG:
    # تأكد من وجود static files للـ admin
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]
