from django.contrib import admin
from contact.models import Contact, Inquiry


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'contact_phone')
    list_editable = ('contact_phone',)
    search_fields = ('contact_name',)


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'message', 'date', 'people')
    search_fields = ('date', 'people', 'name')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Inquiry, InquiryAdmin)
