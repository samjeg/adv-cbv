# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import School, Student

admin.site.register(School)
admin.site.register(Student)  
