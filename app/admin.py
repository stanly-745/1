from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Worker)
admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Expense)
admin.site.register(Income)