from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contact/', include('contact.urls')),
    path('', include('pages.urls')),
    path('menu/', include('menu.urls')),
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
