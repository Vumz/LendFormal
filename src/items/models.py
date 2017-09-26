from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.
COLOR_CHOICES = (
	('BK', 'Black'),
	('WH', 'White'),
	('GY', 'Gray'),
	('RD', 'Red'),
	('BL', 'Blue'),
    ('GR', 'Green'),
    ('OR', 'Orange'),
    ('YW', 'Yellow'),
	('OT', 'Other'),
	('AL', 'ALL'),
	('BR', 'BROWN')
)

GENDER_CHOICES = (
	('ML', 'Male'),
	('FM', 'Female'),
	('OT', 'Other')
)

class Item(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
	name = models.CharField(max_length=30)
	size = models.PositiveSmallIntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	color = models.CharField(max_length=2, choices=COLOR_CHOICES, default='OT')
	description = models.TextField(max_length=500, help_text = "Enter description here!")
	file = models.FileField(upload_to = 'templates')
	collat = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='OT')

	class Meta:
		ordering = ["size", "-name"]

	def __str__(self):              # __unicode__ on Python 2
		return self.name + " " + str(self.size)
