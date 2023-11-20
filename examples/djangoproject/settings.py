from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-njgub0rp7*nm0lm&*sk33g$ujb5=)7r6s6j4&rp!d)u=rdplp%'
DEBUG = True

WSGI_APPLICATION = 'djangoproject.wsgi.application'
STATIC_URL = 'static/'
ROOT_URLCONF = 'djangoproject.urls'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party
    'rest_framework',
    'modern_drf_dark',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'modern_drf_dark.renderers.DarkHorizonBrowsableAPIRenderer',
    )
}

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware', #
    'django.contrib.auth.middleware.AuthenticationMiddleware', #
    'django.contrib.messages.middleware.MessageMiddleware', #
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
