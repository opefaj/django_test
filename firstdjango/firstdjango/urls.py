from django.conf.urls import include, url
from django.contrib import admin
from inventory import views

urlpatterns = [
    # r'^$ is just a /, \d+ matches any integer
#regular expression, view to call if theres a match, name parameter for template
 #starts from the top, goes down if false. no patterns left = 4040 page
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
#default
    url(r'^admin/', include(admin.site.urls)),
]
