from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    fields = ('subscription_plan', 'lineitem_total') 
    readonly_fields = ('lineitem_total',)   
    extra = 0  

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'full_name', 'email', 'phone_number', 'country', 'date', 'order_total')
    search_fields = ('order_number', 'full_name', 'email')
    list_filter = ('date',)
    readonly_fields = ()
    ordering = ('-date',)
    inlines = [OrderLineItemInline]  



admin.site.register(Order, OrderAdmin)


