
from django.contrib import admin
from .models import Customer,Vehicle,User,Page, Worker, Machine 
# Register your models here.
admin.site.register(Customer) 
admin.site.register(Vehicle)

admin.site.register(User)
admin.site.register(Page)

admin.site.register(Worker)
admin.site.register(Machine)