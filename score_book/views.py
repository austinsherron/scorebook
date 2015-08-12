################################################################################
## IMPORTS #####################################################################
################################################################################


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
	"""
	user = request.user

	student = get_query(Student, user=user)
	if student:
		request.session['student'] = student										# add identifier to session for later use
		return redirect('student_landing')											# redirect as student if user is both student and instructor

	instructor = get_query(Instructor, user=user)
	if instructor:
		request.session['instructor'] = instructor							# add identifier to session for later use
		return redirect('instructor_landing')

	request.session['error'] = 'You aren\'t in the scorebook database. Please contact your TA.'
	return redirect('../')																		# redirect to index with error if user isn't student or instructor


@login_required
def student_landing(request):
	"""
	Defines view for student landing page.
	"""
	student = request.session['student']
	context = {'student': student}
	return render(request, 'student_landing_page.html', context)


@login_required
def instructor_landing(request):
	if not confirm_session(request.session, 'instructor'):
		request.session['error'] = 'You are not authorized to view that page.'
		return redirect('../')

	instructor = request.session['instructor']
	context = {'instructor': instructor}
	return render(request, 'instructor_landing_page.html', context)


################################################################################
################################################################################
################################################################################
