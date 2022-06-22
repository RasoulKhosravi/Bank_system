from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=264, unique=True)

class BankBranch(models.Model):
    name = models.CharField(max_length=264, unique=True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)

class Atm(models.Model):
    name = models.CharField(max_length=264, unique=True)
    bank_branch_id = models.ForeignKey(BankBranch, on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=264, unique=True)

class Account(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    bank_branch_id = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Employee(models.Model):
    name = models.CharField(max_length=264, unique=True)
    operation = models.CharField(max_length=264, unique=True)
    bank_branch_id = models.ForeignKey(BankBranch, on_delete=models.CASCADE)

class Transaction(models.Model):
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    bank_branch_id = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    operation = models.CharField(max_length=264, unique=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2)