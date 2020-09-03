# drf-narito-gallery

[ギャラリーサイト](https://github.com/naritotakizawa/vue-narito-gallery)の、Django Rest frameworkで作ったREST APIの実装

## インストール

```
pip install https://github.com/naritotakizawa/drf-narito-gallery/archive/master.tar.gz
```

settings.pyに足す

```python
INSTALLED_APPS = [
    ...
    'ngallery.apps.NgalleryConfig',
    'django_cleanup.apps.CleanupConfig',  # 必須ではないがおすすめ
    'rest_framework',
    'adminsortable2',
]

# 環境によって書き換えて
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

urls.pyに足す

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include('ngallery.urls')),  # お好きなパスで！
]

# これは開発環境用
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
```

また、オリジンが異なる場合は次のような設定も必要になるでしょう。settings.pyに追加

```python
# pip install django-cors-headers
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    '他に必要なIPアドレスやドメイン'
)
```

