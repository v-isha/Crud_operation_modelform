from django.contrib import admin
from regdepartment.models import customer


# Register your models here.
@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display =('customer_id','name','email','password')
 