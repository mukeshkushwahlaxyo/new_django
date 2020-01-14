from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import AddEmployee
from django.contrib.auth.models import User
from employee.forms import SignUpForm
from rolepermissions.roles import assign_role
from rolepermissions.roles import get_user_roles
from django.contrib.auth.decorators import login_required

class Employees:

	@login_required
	def index(request):		
		return render(request, "employees/index.html")

	def EmployeeCreate(request):	
		form = SignUpForm()
		return render(request, "registration.html",{'form':form})
		# if request.POST:
		# 	if form.is_valid():
		# 		user = form.save()
		# 		raw_password = form.cleaned_data.get('password1')
		# 		user = authenticate(username=user.username, password=raw_password)
		# 		# user = User.objects.get(id=1)
		# 		# assign_role(user, 'is_employee')
		# 		login(request, user)
		# 		if request.user.is_authenticated:
		# 			role = get_user_roles(request.user)
		# 			# return HttpResponse(role)
		# 			# return HttpResponse(request.user.username)
		# 			return redirect('/employee')
		# 	else:
		# 		return render(request, "registration.html",{'form':form})
		# else:
		# 	return render(request, "registration.html",{'form':form})	