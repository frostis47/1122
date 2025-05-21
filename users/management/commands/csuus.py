from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Создает тестового пользователя.'

    def handle(self, *args, **options):
        try:
            user = User.objects.create(
                email="User@example.com",
                password="12345",
                is_active=True,
                is_staff=False,
                is_superuser=False
            )
            self.stdout.write(self.style.SUCCESS('Тестовый пользователь успешно создан'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при создании пользователя: {e}'))