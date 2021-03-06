"""Django settings for autodonate project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from pathlib import Path
from secrets import token_urlsafe
from socket import gethostbyname_ex, gethostname

import dj_database_url
import django_stubs_ext
from decouple import config

# Monkeypatching Django, so stubs will work for all generics,
# https://github.com/typeddjango/django-stubs#i-cannot-use-queryset-or-manager-with-type-annotations
django_stubs_ext.monkeypatch()

# RUN_ID is needed to control caching of static files.
# If the server is rebooted, then it changes and clients have to re-download the static assets.
# It is used in its own implementation of static templatetag.
RUN_ID = token_urlsafe(4)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="super-secret-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)
# SECURITY WARNING: Turn it only if you testing in Docker. NOT IN PRODUCTION!
DOCKER = config("DOCKER", default=False, cast=bool)

ALLOWED_HOSTS = [config("HOST", default="*")]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "axes",
    "autodonate",
    "autodonate.lib",
    "index.apps.IndexConfig",
]

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    INSTALLED_APPS.append("nplusone.ext.django")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    # debug_toolbar should be the first.
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    MIDDLEWARE.append("querycount.middleware.QueryCountMiddleware")
    MIDDLEWARE.append("nplusone.ext.django.NPlusOneMiddleware")

# `axes` should be the last item.
MIDDLEWARE.append("axes.middleware.AxesMiddleware")

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first.
    "axes.backends.AxesBackend",
    # Django ModelBackend is the default authentication backend.
    "django.contrib.auth.backends.ModelBackend",
]

# Enable detailed debug only for localhost.
INTERNAL_IPS = [
    "127.0.0.1",
]

# If we in docker, use correct INTERNAL_IPS value.
if DEBUG and DOCKER:
    hostname, _, ips = gethostbyname_ex(gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

ROOT_URLCONF = "autodonate.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "autodonate.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASE_URL = config("DATABASE_URL", default="sqlite:///db.sqlite3")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = config("LANGUAGE_CODE", default="ru-ru")

TIME_ZONE = config("TIME_ZONE", default="Europe/Moscow")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
