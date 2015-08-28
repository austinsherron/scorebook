################################################################################
## IMPORTS #####################################################################
################################################################################


from datetime import datetime as dt
from datetime import timedelta as td
from django.shortcuts import redirect


################################################################################
################################################################################
################################################################################


################################################################################
## HELPRS ######################################################################
################################################################################


def get_query(model, **kwargs):
	"""
	Function that encapsulates the process of making get queries.

	Args:
		model = model object (inherits from Model.model)
		kwargs = args to use in query

	Returns:
		Result of query, or False if there are no results
	"""
	try:
		return model.objects.get(**kwargs)
	except model.DoesNotExist:
		return False


def filter_query(model, **kwargs):
	"""
	Function that makes a filter query on the 
	specified model with the specified keyword args.
	If there are problems making the query or there
	are no results, False is returned.

	Args:
		model = model object( inherits from Model.model)
		kwargs = args to use in query

	Returns:
		Results of query, if they exist, False is
		they don't or any exception is thrown by
		the query.
	"""
	try:
		result = model.objects.filter(**kwargs)
	except:
		return False

	if len(result) == 0:
		return False

	return result


def start_session(request, **kwargs):
	"""
	Function that begins session by adding necessary values
	to request's session dict.

	Args:
		request = request object
		kwargs = key/val pairs to put in seesion dict

	Returns:
		request object
	"""
	for k,v in kwargs.items():
		request.session[k] = v

	return request


def confirm_session(request, admin=None):
	"""
	Function that validates sessions by checking
	to see if login has expired, or if the user is
	valid to view admin areas.

	Args:
		request = request object
		admin = str (key in session)

	Returns:
		response obejct, if session is invalid, else None
	"""
	if admin and admin not in request.session:
		request.session['error'] = 'You are not authorized to view that page'
		return redirect('../')

	if 'login_time' in request.session: 
		if request.session['login_time'] < dt.now() - td(hours=1):
			return redirect('../logout')
	else:
			return redirect('../logout')


def request_to_context(context, request, *args):
	"""
	This method checks to see if the strs in args
	are present in request.session. If they are,
	they are put into context under the same name.
	
	Args:
		context = dict
		request = request object
		args = strs

	Returns:
		context = dict
	"""
	for arg in args:
		if arg in request.session:
			context[arg] = request.session[arg]
		else:
			context[arg] = False

	return context


################################################################################
################################################################################
################################################################################
