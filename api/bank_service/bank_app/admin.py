from django.contrib import admin

from bank_app.models import Atm, Bank, BankBranch, Customer, CustomerRegister, Employee, Transaction

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Atm)
admin.site.register(Bank)
admin.site.register(BankBranch)
admin.site.register(CustomerRegister)
admin.site.register(Transaction)


