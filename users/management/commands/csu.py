from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Создает суперпользователя с электронной почтой Admin@yandex.ru и паролем qwe12345'

    def handle(self, *args, **options):
        try:
            User.objects.get(email="Admin@yandex.ru")
            self.stdout.write(self.style.WARNING("Суперпользователь с электронной почтой Admin@yandex.ru уже существует."))
            return
        except User.DoesNotExist:
            pass

        user = User.objects.create(email="Admin@yandex.ru")
        user.set_password("qwe12345")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS("Суперпользователь успешно создан."))

