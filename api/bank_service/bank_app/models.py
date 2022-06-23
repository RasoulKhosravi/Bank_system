from decimal import Decimal
from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.name

class BankBranch(models.Model):
    name = models.CharField(max_length=264, unique=True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " ("+self.bank_id.name+")"

class Atm(models.Model):
    name = models.CharField(max_length=264, unique=True)
    bank_branch_id = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " ("+self.bank_branch_id.name+")"

class Customer(models.Model):
    name = models.CharField(max_length=264, unique=True)
    def __str__(self):
        return self.name

class Account(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bank_branch_id = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    def __str__(self):
        return self.customer_id.name
    

class Employee(models.Model):
    name = models.CharField(max_length=264, unique=True)
    operation = models.CharField(max_length=264, unique=True)
    bank_branch_id = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " ("+self.bank_branch_id.name+ self.operation+")"


class Transaction(models.Model):
    class TransactionOperation(models.TextChoices):
        CARD_TO_CARD = 'card_to_card', 'Card to Card'
        WITHDRAW = 'withdraw', 'Withdraw'
        DEPOSIT = 'deposit', 'Deposit'

    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    bank_branch_id = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    operation = models.CharField(max_length=264, choices=TransactionOperation.choices,unique=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return self.operation + " TO " + self.account_id.customer_id.name + " IN " + self.bank_branch_id.name