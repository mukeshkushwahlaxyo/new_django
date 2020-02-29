from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
from leavemanagement.forms import LeaveApplyForm
from leavemanagement.models import LeaveTypeModel,LeaveAllotment,LeaveApply
from employee.models import User
from rolepermissions.roles import assign_role
from rolepermissions.roles import get_user_roles
from django.contrib.auth.decorators import login_required
from employee.decorators import is_admin,is_employee,is_manager,is_hr

class HomePage:

	@login_required
	def index(request):		
		return render(request, "home.html")

	def login(request):		
		form = AuthenticationForm()
		if request.user.is_authenticated:
			return redirect("/dashboard")
		else:
			return render(request, "login.html",{'form':form})

	
	def checkLogin(request):
		error = {}
		form = AuthenticationForm(request.POST)
		if request.POST:
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(username=username, password=password)
			login(request, user)
			if request.user.is_authenticated:
				return redirect('/employee')
	@is_admin			
	def Singhup(request):
		form = SignUpForm		
		return render(request, "registration.html",{'form':form})

	@is_admin	
	def Store(request):	
		form = SignUpForm(request.POST)
		if request.POST:
			if form.is_valid():
				user = form.save()
				# form.refresh_from_db()
				raw_password = form.cleaned_data.get('password1')
				# user = authenticate(username=user.username, password=raw_password)
				# user = User.objects.get(id=1)
				# assign_role(user, 'is_employee')
				# login(request, user)
				if request.user.is_authenticated:
					role = get_user_roles(request.user)
					# return HttpResponse(role)
					# return HttpResponse(request.user.username)
					return redirect('/employee')
			else:
				return render(request, "registration.html",{'form':form})
		else:
			return render(request, "registration.html",{'form':form}) 	

	def employeesIndex(request):
		return render(request, "employee/index.html")				

	def getAlldata(request):
		return HttpResponse(request.POST['model'])
	
	def ApplyLeave(request):
		form = LeaveApplyForm()
		users = User.objects.all()
		leaves = LeaveTypeModel.objects.all()
		leaves_id = []
		leave_allot = LeaveAllotment.objects.filter(user_id = request.user.id)
		
		for i in leave_allot:
			if int(i.inital_bal) > 0:
				leaves_id.append(i.leave_mast_id_id)

		if request.method == 'POST':
			form = LeaveApplyForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/employee/show_leave')
			else:
				form = LeaveApplyForm(request.POST)
				return render(request,'employees/leaveApply/create.html',{'form':form,'users':users,'leaves_id':leaves_id,'leaves':leaves})
		else:
			return render(request,'employees/leaveApply/create.html',{'form':form,'users':users,'leaves_id':leaves_id,'leaves':leaves})

	def EditApplyLeave(request,id):
		data = LeaveApply.objects.get(id = id)
		form = LeaveApplyForm(instance = data)
		users = User.objects.all()
		leaves = LeaveTypeModel.objects.all()
		leaves_id = []
		leave_allot = LeaveAllotment.objects.filter(user_id = request.user.id)
		
		for i in leave_allot:
			if int(i.inital_bal) > 0:
				leaves_id.append(i.leave_mast_id_id)

		if request.method == 'POST':
			form = LeaveApplyForm(request.POST,instance=data)
			if form.is_valid():
				form.save()
				return redirect('/employee/show_leave')
			else:
				return render(request,'employees/leaveApply/edit.html',{'form':form,'users':users,'leaves_id':leaves_id,'leaves':leaves,'id':id})
		else:
			return render(request,'employees/leaveApply/edit.html',{'form':form,'users':users,'leaves_id':leaves_id,'leaves':leaves,'id':id})		

	@is_employee		
	def ShowLeaves(request):
		leaves_deatils = LeaveApply.objects.filter(user = request.user.id)
		return render(request,'employees/leaveApply/index.html',{'data':leaves_deatils})

	def DeleteLeave(request,id):
		leave = LeaveApply.objects.get(id = id)	
		leave.delete()
		return redirect('/employee/show_leave')

	@is_admin	
	def ManageRoles(request):
		users = User.objects.all()
		return render(request,'roles.html',{'users':users})

	@is_admin	
	def AssignRole(request):
		id = request.POST.get('id')
		role = request.POST.get('role')
		status = request.POST.get('status')
		userUpdate = User.objects.get(id = id)
		if role == 'is_employee':
			userUpdate.is_employee = status
			userUpdate.save()
		if role == 'is_admin':
			userUpdate.is_admin = status
			userUpdate.save()		
		if role == 'is_hr':
			userUpdate.is_hr = status
			userUpdate.save()		
		if role == 'is_manager':
			userUpdate.is_manager = status
			userUpdate.save()		
		userUpdate.save()	
		return HttpResponse(status = 200)

	def logout_view(request):
		logout(request)			
		return redirect('/')
    	


