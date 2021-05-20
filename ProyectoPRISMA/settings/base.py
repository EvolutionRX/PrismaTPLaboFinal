"""
Django settings for ProyectoPRISMA project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


from pathlib import Path
import os 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0=k(5)!gnn(3p#z=&%tg7_^t^tz)2mfd24y=4xv96v4w0qe^3h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Application definition

INSTALLED_APPS = [
    'material',
    'material.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'widget_tweaks',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuario',
    'item',
    'sucursal',
    'proveedor',
    'mediodepago',
    'django_celery_beat',
    'cliente',
    'venta',
    'presupuesto',
    
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MATERIAL_ADMIN_SITE = {
    'HEADER':  ('Prisma Technology'),  # Admin site header
    'TITLE':  ('Prisma Technology'),  # Admin site title
    'FAVICON':  'imgAdmin/logo.ico',  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR':  'orange',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  'black',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE':  'imgAdmin/perfil.png',  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG':  'imgAdmin/fondo.png',  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  'imgAdmin/logo.png',  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  'imgAdmin/fondo.png',  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES':  True,  #  Show default admin themes button
    'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True, # Show instances counts for each model
    'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
        'sites': 'send',
    },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'site': 'contact_mail',
    }
}

 
ROOT_URLCONF = 'ProyectoPRISMA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'ProyectoPRISMA.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#LOGIN_REDIRECT_URL = reverse_lazy('index')
#LOGOUT_REDIRECT_URL = reverse_lazy('login')

AUTH_USER_MODEL = 'usuario.Usuario'

#CELERY CONFIG

# Celery Configuration Options



# Ejecutar cada lunes a las 18 de la tarde


# config del email

EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS= True
EMAIL_PORT = 587
EMAIL_HOST_USER = "tmmzprueba@gmail.com"
EMAIL_HOST_PASSWORD= "tomy1202"