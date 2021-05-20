from django.contrib import messages
from django.shortcuts import render

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				messages.warning(request, 'You are not authorized to view this page')
				return render(request, "public/index.html")
		return wrapper_func
	return decorator