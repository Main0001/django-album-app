from django.shortcuts import render, redirect
from photos.models import Category, Photo

# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context=context)

def category_gallery(request, category):
    categories = Category.objects.all()
    photos = Photo.objects.filter(category__name=category)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context=context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {'photo': photo}
    return render(request, 'photos/photo.html', context=context)


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(pk=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name = data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category, 
            description=data['description'],
            image = image
        )

        return redirect('photos:gallery')

    context = {'categories': categories}
    return render(request, 'photos/add_photo.html', context=context)
