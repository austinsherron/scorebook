################################################################################
## IMPORTS #####################################################################
################################################################################


from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from score_book.helpers import *


################################################################################
################################################################################
################################################################################


################################################################################
## VIEWS #######################################################################
################################################################################


def index(request):
	"""
	Defines view for the landing page of this application.
	This view will change when app is in production: UCI's
	auth system will be used instead of Django's.
	"""
	user = request.user
	context = {'user': user}
	context = request_to_context(context, request, 'student', 'instructor')

	if 'error' in request.session:
		context['error'] = request.session.pop('error')

	if request.method == 'POST':
		if 'login' in request.POST:
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user:
				auth.login(request, user)
				return redirect('../scorebook')
			else:
				context['error'] = 'Username or password is incorrect'
				return render(request, 'login.html', context)
	else:
		return render(request, 'login.html', context)


@login_required
def logout(request):
	"""
	This is a temporary view for development. Logs a user out.
	"""
	if 'student' in request.session:
		request.session.pop('student')

	if 'instructor' in request.session:
		request.session.pop('instructor')

	auth.logout(request)
	return redirect('../')


################################################################################
################################################################################
################################################################################
