from django.test import TestCase
from .models import Item

class TestModels(TestCase):

    def test_item_is_done_default_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_to_string_method(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
