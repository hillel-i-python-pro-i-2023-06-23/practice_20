from apps.users.models import User


def delete_users():
    return User.objects.all().delete()
