from user.models import Profile


def create_profile(backend, user, *args, **kwargs):
    """Создание профиля пользователя для социальной аутентификации"""
    Profile.objects.get_or_create(user=user)
