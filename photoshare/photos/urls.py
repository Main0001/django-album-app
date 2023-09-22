from django.urls import path

from photos.views import gallery, viewPhoto, addPhoto, category_gallery

app_name = 'photos'

urlpatterns = [
    path('', gallery, name='gallery'),
    path('photo/<int:pk>', viewPhoto, name='photo'),
    path('photos/<slug:category>', category_gallery, name='cat_gallery'),
    path('add/', addPhoto, name='add_photo'),
]