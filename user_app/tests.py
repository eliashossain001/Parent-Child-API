from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Parent, Child
from .serializers import ParentSerializer, ChildSerializer

class ParentTests(APITestCase):
    #positive test case
    def test_create_valid_parent(self):
        url = reverse('parent-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'street_address': '123 Main St',
            'city': 'Anytown',
            'state': 'CA',
            'zip_code': '12345'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Parent.objects.count(), 1)
        self.assertEqual(Parent.objects.get().first_name, 'John')

    #negative test case
    def test_create_invalid_parent(self):
        url = reverse('parent-list')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'street_address': '123 Main St',
            'city': 'Anytown',
            'state': 'CA'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Parent.objects.count(), 0)
