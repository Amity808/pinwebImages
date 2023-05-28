from django.contrib.auth.models import User
from .models import Profile

"""
the authenticate() method receives a request object and 
the username and password optional parameters. 
We could use different parameters, but 
we use username and password to make our backend work with 
the authentication framework views right away. 



AUTHENTICATION_BACKENDS = [
 'django.contrib.auth.backends.ModelBackend',
 'you app name.authentication.EmailAuthBackend',
]
let visit our form.py to get clean email or validate one email per user
we need to make sure that two users are not using two email
"""


class EmailAuthBackend:

    # Authenticate using an email address
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def create_profile(backend, user, *args, **kwargs):
    """
    to create user profile for social authentication
    """
    Profile.objects.get_or_create(user=user)


