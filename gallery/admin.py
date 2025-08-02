from django.contrib import admin
from .models import GalleryImage, GalleryCategory

@admin.register(GalleryImage)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'featured', 'date_taken')
    list_filter = ('featured',)
    search_fields = ('description',)

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    pass