from django.contrib import admin

from bank_app.models import Account, Atm, Bank, BankBranch, Customer, Account, Employee, Transaction

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Atm)
admin.site.register(Bank)
admin.site.register(BankBranch)
admin.site.register(Account)
admin.site.register(Transaction)


