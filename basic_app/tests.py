# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import School, Student

class SchoolModelTests(TestCase):

	def testCreateNewSchool(self):
		lengthBefore = len(School.objects.all())

		school = School.objects.create(
			name="Greenford High School",
			principal="Mr. Jones",
			location="Greenford"
		)

		lengthAfter = len(School.objects.all())

		self.assertIs(lengthBefore==lengthAfter, True)

