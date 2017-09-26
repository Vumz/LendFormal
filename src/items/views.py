from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from items.models import Item
from django.http import HttpResponseRedirect
from items.forms import ItemForm, FilterForm
from django.views import generic

# Create your views here.
def list_items(request):
	items = Item.objects.all()
	form = FilterForm()
	if request.method == "POST":
		form = FilterForm(request.POST)
		if form.is_valid():
			color = form.cleaned_data['color']
			if color != 'ALL':
				items = items.filter(color=color)
			size = form.cleaned_data['size']
			if size:
				items = items.filter(size=size)
	return render(request, 'item_list.html', {'form': form, 'items': items})

def my_items(request):
	items = Item.objects.all().filter(owner=request.user)
	form = FilterForm()
	if request.method == "POST":
		form = FilterForm(request.POST)
		if form.is_valid():
			color = form.cleaned_data['color']
			if color != 'ALL':
				items = items.filter(color=color)
			size = form.cleaned_data['size']
			if size:
				items = items.filter(size=size)
	return render(request, 'item_list.html', {'form': form, 'items': items})

class ItemDetails(DetailView):
	template_name = "item_details.html"

	def get(self, request, pk=None):
		if pk == None:
			redirect('/items/')
		else:
			try:
				item = Item.objects.get(id=pk)
			except Item.DoesNotExist:
				raise Http404("Item does not Exist")
		return render(request, "item_details.html", {"item":item})


def new_item(request):
	if request.method == "POST":
		form = ItemForm(request.POST, request.FILES)
		if form.is_valid():
			# if image instanceof png
			# file = request.FILES['file']
			# print (request.FILES)
			# name = None
			for filename, file in request.FILES.iteritems():
				name = request.FILES[filename].name.lower()
				#name = file.name.lower();
			if name.endswith('.png') or name.endswith('.jpg') or name.endswith('.jpeg'):
				item = form.save()
				item.owner = request.user
				item.save()
				return redirect('/items/my/')
	else:
		form = ItemForm()
	return render(request, 'item_form.html', {'form': form})

class PaymentPage(generic.TemplateView):
    template_name = "payment.html"

