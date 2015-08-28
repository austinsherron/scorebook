################################################################################
## IMPORTS #####################################################################
################################################################################


import uuid
from django.contrib.auth.models import User
from django.db import models


################################################################################
################################################################################
################################################################################


################################################################################
## MODELS ######################################################################
################################################################################


class Instructor(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	ucinetid = models.TextField(blank=False, unique=True)
#	email = models.EmailField(blank=False)			# temporarily commented out for development 			
#	first_name = models.TextField(blank=False)
#	last_name = models.TextField(blank=False)
	preferred_name = models.TextField(default='')
	courses = models.ManyToManyField('Course', blank=True)
	sections = models.ManyToManyField('Section', blank=True)
	user = models.ForeignKey(User)

	class Meta:
		ordering = ['ucinetid']
		verbose_name = 'instructor'
		verbose_name_plural = 'instructors'


	def __str__(self):
		return '{}, {} - {} (instructor)'.format(
			self.user.last_name,
			self.user.first_name,
			self.ucinetid)


class Student(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	ucinetid = models.TextField(blank=False, unique=True)
#	email = models.EmailField(blank=False)			# temporarily commented out for development 			
#	first_name = models.TextField(blank=False)
#	last_name = models.TextField(blank=False)
	preferred_name = models.TextField(default='')
	studentid = models.PositiveIntegerField(blank=False, unique=True)
	courses = models.ManyToManyField('Course', blank=True)
	sections = models.ManyToManyField('Section', blank=True)
	user = models.ForeignKey(User)

	class Meta:
		ordering = ['ucinetid']
		verbose_name = 'student'
		verbose_name_plural = 'students'


	def __str__(self):
		return '{}, {} - {}'.format(
			self.user.last_name,
			self.user.first_name,
			self.ucinetid)


class Quarter(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.TextField(blank=False)
	number = models.IntegerField(blank=False)
	start = models.DateField()
	end = models.DateField()

	class Meta:
		ordering = ['number']
		verbose_name = 'quarter'
		verbose_name_plural = 'quarters'


	def __str__(self):
		return '{} - {}'.format(self.name, self.number)


class Course(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	year = models.IntegerField(blank=False)
	full_name = models.TextField(blank=False)
	abbr_name = models.TextField()
	location = models.TextField(blank=True)
	quarter = models.ForeignKey('Quarter')
	instructors = models.ManyToManyField('Instructor', blank=True)
	students = models.ManyToManyField('Student', blank=True)

	class Meta:
		verbose_name = 'course'
		verbose_name_plural = 'courses'


	def __str__(self):
		return '{} ({}, {})'.format(
			self.abbr_name,
			self.quarter.name,
			self.year
		)


class Section(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.TextField(blank=False)
	number = models.IntegerField(blank=False)
	course = models.ForeignKey('Course')
	instructors = models.ManyToManyField('Instructor', blank=True)
	students = models.ManyToManyField('Student', blank=True)

	class Meta:
		verbose_name = 'section'
		verbose_name_plural = 'sections'


	def __str__(self):
		return '{} Section {}'.format(
			self.course.abbr_name,
			self.number
		)


class Assignment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.TextField(blank=False)
	total_value = models.DecimalField(blank=False, max_digits=10, decimal_places=5)
	is_discrete = models.BooleanField(blank=False)
	upper_bound = models.DecimalField(default=0.0, max_digits=10, decimal_places=5)
	lower_bound = models.DecimalField(default=100.0, max_digits=10, decimal_places=5)
	discrete_score_system = models.ForeignKey('DiscreteScoreSystem', blank=True)
	assignment_type = models.ForeignKey('AssignmentType')
	course = models.ForeignKey('Course')

	class Meta:
		verbose_name = 'assignment'
		verbose_name_plural = 'assignments'


class AssignmentType(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.TextField(blank=False)
	weight = models.DecimalField(blank=False, max_digits=10, decimal_places=5)
	course = models.ForeignKey('Course')

	class Meta:
		verbose_name = 'assignment type'
		verbose_name_plural = 'assignments types'


class ContinuousScore(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	value = models.DecimalField(blank=False, max_digits=10, decimal_places=5)
	assignment = models.ForeignKey('Assignment')
	student = models.ForeignKey('Student')

	class Meta:
		verbose_name = 'score'	
		verbose_name_plural = 'scores'


class DiscreteScore(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	assignment = models.ForeignKey('Assignment')
	student = models.ForeignKey('Student')
	value = models.ForeignKey('DiscreteScoreType')

	class Meta:
		verbose_name = 'score'
		verbose_name_plural = 'scores'


class DiscreteScoreSystem(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	course = models.ForeignKey('Course')
	possible_values = models.ManyToManyField('DiscreteScoreType')

	class Meta:
		verbose_name = 'score system'
		verbose_name_plural = 'score systems'


class DiscreteScoreType(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	numeric_value = models.DecimalField(max_digits=10, decimal_places=5)
	text_value = models.TextField()
	image_value = models.ImageField()
	real_value = models.DecimalField(max_digits=10, decimal_places=5)
	course = models.ForeignKey('Course')
	score_system = models.ManyToManyField('DiscreteScoreSystem', blank=True)

	class Meta:
		verbose_name = 'score type'
		verbose_name_plural = 'score types'


################################################################################
################################################################################
################################################################################
