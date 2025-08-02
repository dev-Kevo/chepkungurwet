# views.py
from django.shortcuts import render, get_object_or_404
from .models import GalleryImage, GalleryCategory

def gallery(request):
    images = GalleryImage.objects.all().order_by('-date_taken')
    categories = GalleryCategory.objects.all().order_by('order')
    
    context = {
        "images": images,
        "categories": categories
    }
    return render(request, 'gallery/gallery.html', context)

def gallery_detail(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    related_images = GalleryImage.objects.filter(
        category=image.category
    ).exclude(pk=pk)[:4]
    
    context = {
        "image": image,
        "related_images": related_images
    }
    return render(request, 'gallery/gallery_detail.html', context)