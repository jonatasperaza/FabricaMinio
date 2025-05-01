# Django com Minio

Este tutorial mostra como configurar o Minio em uma aplicação Django para armazenar arquivos estáticos e de mídia.

## O que é Minio?

Minio é um serviço de armazenamento de objetos de código aberto que oferece uma alternativa para o Amazon S3. Ele é ideal para armazenar arquivos como imagens, vídeos, backups, containers e outros tipos de dados não estruturados.

---

## 1. Instalar o pacote django-minio-storage

Primeiro, instale o pacote django-minio-storage usando pip:

```bash
pdm add django-minio-storage
```

## 2. Adicionar ao INSTALLED_APPS

Adicione `minio_storage` às aplicações instaladas no arquivo `settings.py` do seu projeto Django:

```python
INSTALLED_APPS = [
    # ... outras aplicações
    "minio_storage",
]
```

## 3. Configurar as variáveis de ambiente

Você pode definir as configurações do Minio no arquivo `settings.py` do seu projeto Django. Abaixo está um exemplo usando variáveis de ambiente (recomendado para segurança):

```python
import os

# Configurações do Minio
MINIO_STORAGE_ENDPOINT = os.getenv("MINIO_STORAGE_ENDPOINT", "minio.fabricadesoftware.ifc.edu.br")
MINIO_STORAGE_ACCESS_KEY = os.getenv("MINIO_STORAGE_ACCESS_KEY", "my_access_key")
MINIO_STORAGE_SECRET_KEY = os.getenv("MINIO_STORAGE_SECRET_KEY", "my_secret_key")
MINIO_STORAGE_USE_HTTPS = os.getenv("MINIO_STORAGE_USE_HTTPS", "True") == "True"
MINIO_PUBLIC_URL = os.getenv("MINIO_PUBLIC_URL", "minio.fabricadesoftware.ifc.edu.br")

# Configurar o Minio como armazenamento padrão
DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"

# Nome do bucket e criação automática
MINIO_STORAGE_MEDIA_BUCKET_NAME = "my_bucket"
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True

# Se quiser um bucket separado para arquivos estáticos mas é totalmente opcional
MINIO_STORAGE_STATIC_BUCKET_NAME = "my_static_bucket"
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
```

## 4. Configurar modelo para armazenar arquivos

Para usar o Minio em um modelo que armazena arquivos, você precisa especificar o `MinioMediaStorage` como o storage para o campo `FileField` ou `ImageField`. Exemplo:

```python
from django.db import models
from minio_storage.storage import MinioMediaStorage

class Archive(models.Model):
    """
    Exemplo de model que armazena arquivos usando MinioMediaStorage.
    """
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(storage=MinioMediaStorage)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
```

> **Observação:** A classe `MinioMediaStorage` é usada diretamente sem instanciação (sem parênteses), como mostrado acima.

## 5. Migrar o banco de dados

Após configurar o modelo, execute as migrações para aplicar as alterações:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Usar com Django REST Framework

O pacote django-minio-storage faz a maior parte do trabalho pesado automaticamente. Você não precisa de código especial para lidar com o armazenamento, pois a configuração que fizemos nos settings e no modelo já trata disso. Com Django REST Framework, você pode usar ViewSets e Serializers padrão:

### 6.1 Exemplo de Serializer:


```python
from rest_framework import serializers
from core.uploader.models import Archive


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ["id", "titulo", "arquivo", "criado_em"]
        read_only_fields = ["id", "criado_em"]
```

### 6.2 Exemplo de ViewSet:

```python
from rest_framework import viewsets
from core.uploader.models import Archive
from core.uploader.serializers import ArchiveSerializer


class ArchiveViewSet(viewsets.ModelViewSet):
    """
    ViewSet para CRUD de Arquivos.
    - list, retrieve, create, update, destroy
    """

    queryset = Archive.objects.all().order_by("-criado_em")
    serializer_class = ArchiveSerializer
```

### 6.3 Configurando as URLs:

```python
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.uploader.views import ArchiveViewSet

router = DefaultRouter()
router.register('archives', ArchiveViewSet)

urlpatterns = [
    # ...outras URLs
    path('api/', include(router.urls)),
]
```

