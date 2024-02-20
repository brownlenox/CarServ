from django.contrib import admin
from .models import Booking, RemainingItem

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_email', 'service', 'service_date']
    search_fields = ['user_name', 'user_email', 'service']


@admin.register(RemainingItem)
class RemainingItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'remaining_quantity', 'note')
    list_editable = ('remaining_quantity', 'note')
    search_fields = ('item_name', 'note')


admin.site.site_header = "CarServ"
admin.site.site_title = "CarServ"

