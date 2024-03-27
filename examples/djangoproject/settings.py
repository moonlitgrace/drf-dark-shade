from pathlib import Path
import os

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
    # package should be at bottom of your apps
    'drf_dark_shade',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'drf_dark_shade.renderers.DeepForestBrowsableAPIRenderer',
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
        # configure root templates
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
