from django.test import TestCase 
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=5,title="Rice and Beans", price=15, inventory=100)
        self.assertEqual(item.title, "Rice and Beans")
        self.assertEqual(item.price, 15)