from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from decimal import Decimal
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=Decimal('80'), inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

