from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bank_app.models import Account, Transaction
from bank_app.serializers import AccountSerializer, TranactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
   queryset = Transaction.objects.all()
   serializer_class = TranactionSerializer

class AccountViewSet(viewsets.ModelViewSet):
   queryset = Account.objects.all()
   serializer_class = AccountSerializer