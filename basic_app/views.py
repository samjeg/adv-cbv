# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (
									View, 
									TemplateView, 
									ListView, 
									DetailView,
									CreateView,
									UpdateView,
									DeleteView
								)
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from . import models


class IndexView(TemplateView):
	template_name = 'index.html'

class SchoolListView(ListView):
	context_object_name = 'school_list'
	model = models.School
	template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
	context_object_name = 'school_detail'
	model = models.School
	template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
	fields = ('name', 'principal', 'location')
	model = models.School
	template_name = 'basic_app/school_create.html'

class SchoolUpdateView(UpdateView):
	fields = ('name', 'principal')
	model = models.School
	template_name = 'basic_app/school_create.html'

class SchoolDeleteView(DeleteView):
	model = models.School
	success_url = reverse_lazy('basic_app:list')
	template_name = 'basic_app/school_delete_confirm.html'


