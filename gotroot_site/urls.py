from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('master/', admin.site.urls),
    path('', include('shop.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('cart/', include('cart.urls')),
    path('board/', include('board.urls')),
    path('flag/', include('flag.urls')),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)