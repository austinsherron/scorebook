################################################################################
## IMPORTS #####################################################################
################################################################################


from datetime import datetime as dt
from datetime import timedelta as td
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from score_book.helpers import *
from score_book.models import *


################################################################################
################################################################################
################################################################################


################################################################################
## VIEWS #######################################################################
################################################################################


@login_required
def landing(request):
	"""
	Defines view for user landing page. This view redirects
	based on type of user.

	TODO:
		DONE: Handle cases where user is both student and instructor
	"""
	user = request.user

	student = get_query(Student, user=user)
	instructor = get_query(Instructor, user=user)

	if student and instructor:
		request = start_session(request, student=student, instructor=instructor, login_time=dt.now())	
		return redirect('instructor_landing')				# redirect as instructor if user is both student and instructor

	elif instructor:
		request = start_session(request, instructor=instructor, login_time=dt.now())	
		return redirect('instructor_landing')

	elif student:
		request = start_session(request, student=student, login_time=dt.now())	
		return redirect('student_landing')

	request.session['error'] = 'You aren\'t in the scorebook database. Please contact your TA.'
	return redirect('../')												# redirect to index with error if user isn't student or instructor


@login_required
def student_landing(request):
	"""
	Defines view for student landing page.

	TODO:
		DONE: Fix student error condition (61)
	"""
	session_not_valid = confirm_session(request)
	if session_not_valid:
		return session_not_valid

	if 'student' not in request.session:
		return redirect('landing')

	context = request_to_context({}, request, 'student')
	return render(request, 'student_landing_page.html', context)


@login_required
def instructor_landing(request):
	"""
	Defines view for instructor landing page.
	"""
	session_not_valid = confirm_session(request, 'instructor')
	if session_not_valid:
		return session_not_valid

	context = request_to_context({}, request, 'instructor')
	context['courses'] = filter_query(Course, year=2014)
	return render(request, 'instructor_landing_page.html', context)


################################################################################
################################################################################
################################################################################
