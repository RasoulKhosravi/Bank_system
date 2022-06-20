from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from bank_app.models import Transaction
from bank_app.serializers import TranactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
   queryset = Transaction.objects.all()
   serializer_class = TranactionSerializer