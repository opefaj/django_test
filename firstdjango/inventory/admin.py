from django.contrib import admin
from .models import Item
# Register your models here.
#import item models
#class to customize admin interface
#modeladmin to define model classes
class ItemAdmin(admin.ModelAdmin):
	#this basically changes the display in the admin window
	list_display = ['title', 'amount']
admin.site.register(Item, ItemAdmin)