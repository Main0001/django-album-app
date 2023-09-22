from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return f'category: {self.name}'
        
class Photo(models.Model):
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'photos description: {self.description}'

    def get_absolute_url(self):
        return reverse('photos:photo', kwargs={'pk': self.pk})