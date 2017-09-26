from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'items/$', views.list_items, name='items'),
	url(r'^items/new/$', views.new_item, name='new_item'),
	url(r'^items/my/$', views.my_items, name='wardrobe'),
	url(r'^payment/$', views.PaymentPage.as_view(), name='payment'),
    url(r'^items/details/(?P<pk>[0-9]+)/$', views.ItemDetails.as_view(), name='item_details'),

]
