from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from employee.models import User
from hrd.models import Employee,TypesMast,StatusMast,GradesMast,DesigMast,ComapnyMast,AcademicsMast
from employee.forms import SignUpForm,EmployeeEditForm
from hrd.forms import PersonalInfo,OfficeInfo,AcademicsInfo,BankInfo,Documents
from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role
from rolepermissions.roles import get_user_roles
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

class Employees:

	@login_required
	def index(request):		
		# if has_role(request.user,'is_employee'):
		# 	return HttpResponse('role')
		user = User.objects.all()
		return render(request, "employees/index.html",{'user':user})

	@login_required	
	def EmployeeCreate(request):	
		form = SignUpForm()
		return render(request, "registration.html",{'form':form})

	# @login_required
	def saveEmployee(request):	
		form = SignUpForm(request.POST)
		if request.POST:
			if form.is_valid():
				user1 = form.save()
				assign_role(user1, 'is_employee')
				emp = Employee(user_id=user1.id)
				emp.save()
				# form.refresh_from_db()
				# raw_password = form.cleaned_data.get('password1')
				# user = authenticate(username=user1.username, password=raw_password)
				 # user = User.objects.get(id=1)
			
				# login(request, user)
				return redirect('/hrd/employees')
				# if request.user.is_authenticated:
					
					# role = get_user_roles(user)
					# return HttpResponse(role)
					# return HttpResponse(request.user.username)
					
			else:
			 	 return render(request, "registration.html",{'form':form})
		else:
			return render(request, "registration.html",{'form':form}) 

	@login_required		
	def deleteEmployee(request,id):
		user = User.objects.get(pk=id)
		group = Group.objects.get(name='is_employee') 
		user.groups.remove(group)
		user.delete();
		return redirect('/hrd/employees')

	@login_required
	def editEmployee(request,id=''):
		if request.method=='POST':
			data = User.objects.get(id=id)
			form = EmployeeEditForm(request.POST,instance = data)		
			if form.is_valid():
				form.save();
				return redirect('/hrd/employees')
		else:
			data = User.objects.get(id=id)
			form = EmployeeEditForm(instance = data)
			return render(request, "employees/edit.html",{'form':form,'id':id})

	@login_required
	def showTabs(request,page,id):
		employee = Employee.objects.get(user_id=id)		
		if page == 'main':
			main = render(request, "employees/empinfo.html",{'id':id})
		if page == 'personal':
			if request.method == 'POST':
				form = PersonalInfo(request.POST)
				if form.is_valid():
					return HttpResponse(form)
				else:
					main = render(request, "employees/forms/personal.html",{'form':form})	
			else:
				form = PersonalInfo()
				main = render(request, "employees/forms/personal.html",{'form':form})	
		if page == 'office':
			form = OfficeInfo()
			main = render(request, "employees/forms/office.html",{'form':form})	
		if page == 'academics':
			form = AcademicsInfo()
			main = render(request, "employees/forms/academics.html",{'form':form})
		if page == 'bankinfo':
			form = BankInfo()
			main = render(request, "employees/forms/bankinfo.html",{'form':form})
		if page == 'document':
			form = Documents()
			main = render(request, "employees/forms/document.html",{'form':form})
		return main
