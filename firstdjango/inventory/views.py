from django.shortcuts import render
from inventory.models import Item #use to query databse
from django.http import Http404 #to return 404 page when needed
# Create your views here.
def index(request):
	items = Item.objects.exclude(amount=0)
	return render(request, 'inventory/index.html', {'items': items,})

	#creates http response and wires view to template
	#name of var in template, value from query set
def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)#look for utem matching that id
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'inventory/item_detail.html', {'item':item,})
	#views take a response, and id but depends