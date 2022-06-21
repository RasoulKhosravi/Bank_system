from pyexpat import model
from rest_framework import serializers

from bank_app.models import Account, Employee, Transaction

class TranactionSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        operations = ['withdraw', 'deposit']
        if attrs['operation'] not in  operations:
            raise serializers.ValidationError("your operation is not valid")

        customer_id = attrs['customer_id'].id
        bank_id = attrs['branch_id'].bank_id.id
        account = Account.objects.filter(bank_id = bank_id).filter(customer_id = customer_id)
        if not account:
            raise serializers.ValidationError("you dont have any account in this bank")

        branch_id = attrs['branch_id'].id
        employees = Employee.objects.filter(bank_branch_id = branch_id).filter(operation = attrs['operation'])
        if not employees:
            raise serializers.ValidationError("this operation is not avilable in this branch")

        return attrs

    class Meta:
        model = Transaction
        fields = ('branch_id', 'customer_id', 'atm_id', 'operation', 'amount')

class AccountSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        bank = attrs['bank_id']
        branch = attrs['bank_branch_id']
        if bank.id != branch.bank_id.id:
            raise serializers.ValidationError("this branch is not for this bank")

        customer_id = attrs['customer_id'].id
        account = Account.objects.filter(bank_id = bank.id).filter(customer_id = customer_id)
        if account:
            raise serializers.ValidationError("you have alreday an acconut in this bank")

        employees = Employee.objects.filter(bank_branch_id = branch.id).filter(operation = 'opening_account')
        if not employees:
            raise serializers.ValidationError("this operation is not avilable in this branch")

        return attrs

    class Meta:
        model = Account
        fields = ('bank_id', 'bank_branch_id', 'customer_id')