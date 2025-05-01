import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-$^x8y_vh7@#0snpnbo8e^@!-ar^-pg97-p&de3h(7(r*s@l5*o"


DEBUG = True

ALLOWED_HOSTS = ["*"]

MINIO_STORAGE_ENDPOINT = os.getenv("MINIO_STORAGE_ENDPOINT", "mytb.fabricadesoftware.ifc.edu.br")
MINIO_STORAGE_ACCESS_KEY = os.getenv("MINIO_STORAGE_ACCESS_KEY", "hjnRDeC06UzHcB5hkK2M")
MINIO_STORAGE_SECRET_KEY = os.getenv("MINIO_STORAGE_SECRET_KEY", "3KC9YQKVc5b7F2p1jh1Zd5CY7m0IOZjtuDXzCiPd")
MINIO_STORAGE_USE_HTTPS = os.getenv("MINIO_STORAGE_USE_HTTPS", True)
MINIO_PUBLIC_URL = os.getenv("MINIO_PUBLIC_URL", "mytb.fabricadesoftware.ifc.edu.br")
DEFAULT_FILE_STORAGE = "django_minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE = "django_minio_storage.storage.MinioStaticStorage"
MINIO_STORAGE_MEDIA_BUCKET_NAME = "teste"
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "minio_storage",
    "rest_framework",
    "core.uploader",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
