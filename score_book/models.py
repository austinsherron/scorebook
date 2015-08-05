from django.db import models


class Instructor(models.User):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	ucinetid = models.TextField(blank=False)
	email = models.EmailField(blank=False)
	first_name = models.TextField(blank=False)
	last_name = models.TextField(blank=False)
	courses = models.ManyToManyField(Course)
	sections = models.ManyToManyField(Section)


class Student(models.User):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	ucinetid = models.TextField(blank=False)
	email = models.EmailField(blank=False)
	first_name = models.TextField(blank=False)
	last_name = models.TextField(blank=False)
	studentid = models.PositiveIntegerField(blank=False)
	courses = models.ManyToManyField(Course)
	sections = models.ManyToManyField(Section)


class Quarter(models.User):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.TextField(blank=False)


class Course(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	year = models.IntegerField(blank=False)
	full_name = models.TextField(blank=False)
	abbr_name = models.TextField()
	location = models.TextField()
	quarter = models.ForeignKey(Quarter)
	instructors = models.ManyToManyField(Instructor)
	students = models.ManyToManyField(Student)


class Section(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.TextField(blank=False)
	number = models.IntegerField(blank=False)
	course = models.ForeignKey(Course)
	instructors = models.ManyToManyField(Instructor)
	students = models.ManyToManyField(Student)


class Assignment(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.TextField(blank=False)
	total_value = models.DecimalField(blank=False)
	is_discrete = models.BooleanField(blank=False)
	upper_bound = models.DecimalField(default=0.0)
	lower_bound = models.DecimalField(default=100.0)
	discrete_score_system = models.ForeignKey(DiscreteScoreSystem)
	assignment_type = models.ForeignKey(AssignmentType)
	course = models.ForeignKey(Course)


class AssignmentType(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.TextField(blank=False)
	weight = models.DecimalField(blank=False)
	course = models.ForeignKey(Course)


class ContinuousScore(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	value = models.DecimalField(blank=False)
	assignment = models.ForeignKey(Assignment)
	student = models.ForeignKey(Student)


class DiscreteScore(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	assignment = models.ForeignKey(Assignment)
	student = models.ForeignKey(Student)
	value = models.ForeignKey(DiscreteScoreType)


class DiscreteScoreSystem(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	course = models.ForeignKey(Course)
	possible_values = models.ManyToMany(DiscreteScoreType)


class DiscreteScoreType(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	numeric_value = models.DecimalField()
	text_value = models.TextField()
	image_value = models.ImageField()
	real_value = models.DecimalField()
	course = models.ForeignKey(Course)
	score_system = models.ManyToManyField(DiscreteScoreSystem)



