from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
	model = Contact
	list_display = ['first_name', 'last_name','email', 'useful_email']
	search_fields = ['first_name', 'last_name','email']
	list_filter = ['active']
	
	list_display_links = ['first_name', 'last_name']
	ordering = ['last_name', 'first_name']

admin.site.register(Contact, ContactAdmin)