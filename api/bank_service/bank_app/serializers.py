from pyexpat import model
from rest_framework import serializers

from bank_app.models import Account, Atm, Employee, Transaction

class TranactionSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        operations = ['withdraw', 'deposit', 'card_to_card']

        if attrs['operation'] not in  operations:
            raise serializers.ValidationError("your operation is not valid")

        branch = attrs['bank_branch_id']
        if attrs['operation'] == 'card_to_card':
            atm = Atm.objects.filter(bank_branch_id = branch.id)
            if not atm:
                raise serializers.ValidationError("this branch dosent have any atm")
       
        if attrs['operation'] != 'card_to_card':
            requst_branch_bank_id = branch.bank_id.id
            account_bank_id = attrs['account_id'].bank_branch_id.bank_id.id
            if requst_branch_bank_id != account_bank_id:
                raise serializers.ValidationError("you dont have an account in this bank")

            employees = Employee.objects.filter(bank_branch_id = branch.id).filter(operation = attrs['operation'])
            if not employees:
                raise serializers.ValidationError("this operation is not avilable in this branch")
      
        return attrs

    class Meta:
        model = Transaction
        fields = ('id', 'bank_branch_id', 'account_id', 'operation', 'amount')


class AccountSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        branch = attrs['bank_branch_id']
        customer_id = attrs['customer_id'].id
        account = Account.objects.filter(bank_branch_id = branch.id).filter(customer_id = customer_id)
        if account:
            raise serializers.ValidationError("you have alreday an acconut in this branch")

        employees = Employee.objects.filter(bank_branch_id = branch.id).filter(operation = 'opening_account')
        if not employees:
            raise serializers.ValidationError("this operation is not avilable in this branch")

        return attrs

    class Meta:
        model = Account
        fields = ('id', 'bank_branch_id', 'customer_id')