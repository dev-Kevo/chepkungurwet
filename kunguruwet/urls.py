"""
URL configuration for kunguruwet project.
"""
from django.contrib import admin
from django.urls import include, path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('gallery/', include('gallery.urls')),
    # path('donations/', include('donations.urls')),
    path('mg/', include('dashboard.urls')),
    path('accounts/', include('dashboard.urls')),
]

# handle 404 errors
handler404 = 'core.views.handle_404'
handler500 = 'core.views.handle_500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__reload__/', include('django_browser_reload.urls')),  # For live reloading
    ]