from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Table


User = get_user_model()


class TablesModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", email="test_user@example.com", password="12345")

    def test_creating_table(self):
        table = Table.objects.create(
            number="55",
            sitting=1,
            content="",
            price=3000,
            image="",
            table_occupiers=True,
        )
        self.assertIsInstance(table, Table)
        self.assertEqual(table.number, "55")
        self.assertEqual(table.sitting, 1)
        self.assertEqual(table.content, "")
        self.assertEqual(table.price, 3000)

    def test_table_string_table(self):
        table = Table.objects.create(
            number="55",
            sitting=1,
            content="",
            price=3000,
            image="",
            table_occupiers=True,
        )
        self.assertEqual(str(table), table.number)


class TablesSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", email="test_user@example.com", password="12345")
        self.valid_table_data = {
            "number": "Д55",
            "sitting": 1,
            "content": "",
            "price": 3000,
            "image": "",
            "table_occupiers": True,
        }

    def test_sitting_complete(self):
        invalid_data = self.valid_table_data.copy()
        invalid_data["sitting"] = 8
