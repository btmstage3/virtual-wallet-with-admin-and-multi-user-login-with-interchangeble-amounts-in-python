from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.transaction = Transaction.objects.create(sender=self.user1, receiver=self.user2, amount=100, transaction_type='SEND')

    def test_transaction_model(self):
        self.assertEqual(str(self.transaction), 'user1 -> user2 (100.00)')

    def test_transaction_list_view(self):
        client = APIClient()
        client.force_authenticate(user=self.user1)
        response = client.get('/transactions/')
        transactions = Transaction.objects.filter(sender=self.user1) | Transaction.objects.filter(receiver=self.user1)
        serializer = TransactionSerializer(transactions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transaction_detail_view(self):
        client = APIClient()
        client.force_authenticate(user=self.user1)
        response = client.get(f'/transactions/{self.transaction.id}/')
        serializer = TransactionSerializer(self.transaction)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_transaction_create_view(self):
        client = APIClient()
        client.force_authenticate(user=self.user1)
        data = {'sender': self.user1.id, 'receiver': self.user2.id, 'amount': 200, 'transaction_type': 'SEND'}
        response = client.post('/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 2)
        self.assertEqual(Transaction.objects.last().amount, 200)
