from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            try:
                user = UserModel.objects.get(email=username)
            except (ObjectDoesNotExist, MultipleObjectsReturned):
                pass
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None