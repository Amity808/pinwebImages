from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings


# Create your models here.

class Images(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, blank=True)
    url = models.URLField(max_length=3000)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    # book_file = models.FileField(upload_to='book/%y/%m/%d')

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name="images_liked",
                                        blank=True)

    # to get according to the date created
    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    # setting slug field to tittle
    """We will override the save() method of the Image model to automatically generate the slug field based 
    on the value of the title field. Import the slugify() function and add a save() m"""
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
