from django.contrib import admin
from .models import Destination, Guide, Package, Customer, Booking

admin.site.register(Destination)
admin.site.register(Package)
admin.site.register(Customer)
admin.site.register(Booking)
@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'languages', 'experience')
    search_fields = ('name', 'languages', 'email')