from rest_framework import serializers

from bank_app.models import Transaction


class TranactionSerializer(serializers.ModelSerializer):
   class Meta:
       model = Transaction
       fields = ('bank_id', 'bank_branch_id', 'customer_id', 'atm_id', 'operation', 'amount')