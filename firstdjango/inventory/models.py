from django.db import models

# Create your models here. 
#Models define the structure of database tables
# item, description, number in stock
#allow admins create, edit or delete (to do list)

#class called Item
#Field called title that accepts characters < 200
#Description field uses text field since we do not know the length
#amount field takes in only whole numbers
class Item(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()