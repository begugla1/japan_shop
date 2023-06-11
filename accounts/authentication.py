from accounts.models import Profile


def create_profile(backend, user, *args, **kwargs):
    """
    Создание профиля пользователя для социальной аутентификации
    :param backend:
    :param user:
    :param args:
    :param kwargs:
    :return:
    """
    Profile.objects.get_or_create(user=user)