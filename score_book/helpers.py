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


def confirm_session(session, val):
	"""
	Function that validates sessions by checking
	if the val is in session.

	Args:
		session = dict (from request)
		val = str (key in session)

	Returns:
		bool
	"""
	return val in session


################################################################################
################################################################################
################################################################################
