from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings


# to extend the User model is by creating a 
# profile model that contains a one-to-one relationship 
# with the Django User model, and any additional fields. 
# A one

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'

# Create your models here.


class Contact(models.Model):
    user_from = models.ForeignKey('auth.User', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.user', related_name='rel_from_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


class User(models.Model):
    following = models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)
    user_model = get_user_model()
    user_model.add_to_class(
        'following',

    )