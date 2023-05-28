from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_of_guests', 'bookingDate', )
    search_fields = ("name__startswith", ) 
    

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory',)  
    search_fields = ("title__startswith", ) 