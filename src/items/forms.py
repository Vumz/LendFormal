from django import forms
from items.models import Item, COLOR_CHOICES, GENDER_CHOICES

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('name', 'size', 'color', 'price', 'description', 'file', 'collat', 'gender')

class FilterForm(forms.Form):
	color = forms.ChoiceField(choices=COLOR_CHOICES, required=False)
	size = forms.IntegerField(required=False)
