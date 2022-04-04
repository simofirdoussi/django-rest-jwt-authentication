from django.contrib.auth.backends import ModelBackend
from .models import User
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            #try directly to get the user
            user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except User.DoesNotExist:
            #if the user does not exists we don't enter here
            User.set_password(password)
        except MultipleObjectsReturned:
            #if there are many users with don't enter here
            return User.objects.filter(email=username).order_by('id').first()
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try: 
            user=User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None