from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import AddEmployee
from employee.models import User
from hrd.models import Employee
from employee.forms import SignUpForm
from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role
from rolepermissions.roles import get_user_roles
from django.contrib.auth.decorators import login_required

class Employees:

	@login_required
	def index(request):		
		user = User.objects.all()
		return render(request, "employees/index.html",{'data':user})

	def EmployeeCreate(request):	
		form = SignUpForm()
		return render(request, "registration.html",{'form':form})

	def saveEmployee(request):	
		form = SignUpForm(request.POST)
		if request.POST:
			if form.is_valid():
				user = form.save()
				
				# form.refresh_from_db()
				raw_password = form.cleaned_data.get('password1')
				users = authenticate(username=user.username, password=raw_password)
				 # user = User.objects.get(id=1)
				assign_role(user, 'is_employee')
				login(request, users)
				if request.user.is_authenticated:
					employee = Employee(user_id=user.id)
					employee.save()
					# return HttpResponse(role)
					# return HttpResponse(request.user.username)
					return redirect('/hrd/employees')
			else:
			 	 return render(request, "registration.html",{'form':form})
		else:
			return render(request, "registration.html",{'form':form}) 			