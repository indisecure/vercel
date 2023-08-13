from django.contrib import admin
from .models import Customer,Table
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name','email','mobile','message','date']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display=['id','course','duration']