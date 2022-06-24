from django.contrib import admin

from bank_app.models import Account, Atm, Bank, BankBranch, Customer, Employee, Transaction

class BankBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'bank_id')
    pass

class AtmAdmin(admin.ModelAdmin):
    list_display = ('name', 'bank_branch_id')
    pass

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'operation', 'bank_branch_id')
    pass

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account_id', 'bank_branch_id', 'operation')
    list_filter = [
         "account_id",
         "bank_branch_id",
         "operation"
    ]
    pass
class AccountAdmin(admin.ModelAdmin):
    list_display = ('bank_branch_id', 'customer_id')
    pass

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Atm, AtmAdmin)
admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(BankBranch, BankBranchAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Account, AccountAdmin)