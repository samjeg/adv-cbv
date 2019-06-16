# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class School(models.Model):
	name = models.CharField(max_length=20)
	principal = models.CharField(max_length=20)
	location = models.CharField(max_length=20)
	picture = models.ImageField(upload_to='images', blank=True, null=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('basic_app:detail', kwargs={'pk':self.pk})

class Student(models.Model):
	name = models.CharField(max_length=20)
	age = models.PositiveIntegerField()
	school = models.ForeignKey(School, related_name='students')

	def __str__(self):
		return self.name

