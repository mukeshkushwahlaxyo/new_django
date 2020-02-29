from django.contrib.auth.decorators import login_required, user_passes_test

user_login_required = user_passes_test(lambda user: user.is_admin, login_url='/')
user_login_employee = user_passes_test(lambda user: user.is_employee, login_url='/')
user_login_manager = user_passes_test(lambda user: user.is_manager, login_url='/')
user_login_hr = user_passes_test(lambda user: user.is_hr, login_url='/')

def is_admin(view_func):
	decorated_view_func = login_required(user_login_required(view_func))
	return decorated_view_func

def is_employee(view_func):
	decorated_view_func = login_required(user_login_employee(view_func))
	return decorated_view_func

def is_manager(view_func):
	decorated_view_func = login_required(user_login_manager(view_func))
	return decorated_view_func

def is_hr(view_func):
	decorated_view_func = login_required(user_login_hr(view_func))
	return decorated_view_func			