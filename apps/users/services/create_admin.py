from django.contrib.auth import get_user_model


def create_admin():
    User = get_user_model()

    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser("admin", "admin@gmail.com", "admin123")
        print("Superuser created")
    else:
        print("Superuser already exists")
