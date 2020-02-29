from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from masters.forms import DepartmentForm,DocumentTypeForm,DesignationForm,EmployeeGradeForm,EmployeeStatusForm,EmployeeTypeForm
from masters.models import DepartmentModel,DocumentTypeModel,DesignationModel,EmployeeGrade,EmployeeStatus,EmployeeType
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from employee.decorators import is_admin,is_employee,is_manager,is_hr

class Masters():

	@login_required
	@is_admin
	@is_manager
	@is_hr
	def index(request):
		return render(request,'settings/masters/index.html')

class Department():

	@login_required
	@is_admin
	@is_manager
	@is_hr
	def index(request):
		data = DepartmentModel.objects.all()
		return render(request,'settings/masters/department/index.html',{'data':data})		

	@login_required
	@is_admin
	@is_manager
	@is_hr	
	def create(request):
		if request.method == "POST":
			form = DepartmentForm(request.POST)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = DepartmentModel.objects.all()
				return redirect('/masters/department',{'data':data})	
			else:
				return render(request,'settings/masters/department/create.html',{'form':form})
		else:
			form = DepartmentForm()
			return render(request,'settings/masters/department/create.html',{'form':form})				

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def edit(request,id):
		if request.method == "POST":
			obj = DepartmentModel.objects.get(id=id)
			form = DepartmentForm(request.POST,instance = obj)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = DepartmentModel.objects.all()
				return redirect('/masters/department',{'data':data})	
			else:
				return render(request,'settings/masters/department/edit.html',{'form':form,'id':id})					
		else:
			obj = DepartmentModel.objects.get(id=id)
			form = DepartmentForm(instance=obj)
			return render(request,'settings/masters/department/edit.html',{'form':form,'id':id})

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def delete(request,id):
		depart = DepartmentModel.objects.get(id = id)
		depart.delete()
		messages.add_message(request, messages.INFO, 'Data Deleted Successfully.')
		data = DepartmentModel.objects.all()
		return redirect('/masters/department',{'data':data})

class DocumentType():

	@login_required
	@is_admin
	@is_manager
	@is_hr
	def index(request):
		data = DocumentTypeModel.objects.all()
		return render(request,'settings/masters/document/index.html',{'data':data})		

	@login_required
	@is_admin
	@is_manager
	@is_hr	
	def create(request):
		if request.method == "POST":
			form = DocumentTypeForm(request.POST)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = DocumentTypeModel.objects.all()
				return redirect('/masters/documenttype',{'data':data})	
			else:
				return render(request,'settings/masters/document/create.html',{'form':form})
		else:
			form = DocumentTypeForm()
			return render(request,'settings/masters/document/create.html',{'form':form})				

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def edit(request,id):
		if request.method == "POST":
			obj = DocumentTypeModel.objects.get(id=id)
			form = DocumentTypeForm(request.POST,instance = obj)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = DocumentTypeModel.objects.all()
				return redirect('/masters/documenttype',{'data':data})	
			else:
				return render(request,'settings/masters/document/edit.html',{'form':form,'id':id})					
		else:
			obj = DocumentTypeModel.objects.get(id=id)
			form = DocumentTypeForm(instance=obj)
			return render(request,'settings/masters/document/edit.html',{'form':form,'id':id})

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def delete(request,id):
		depart = DocumentTypeModel.objects.get(id = id)
		depart.delete()
		messages.add_message(request, messages.INFO, 'Data Deleted Successfully.')
		data = DocumentTypeModel.objects.all()
		return redirect('/masters/documenttype',{'data':data})		

class Designation():

	@login_required
	@is_admin
	@is_manager
	@is_hr
	def index(request):
		data = DesignationModel.objects.all()
		return render(request,'settings/masters/designation/index.html',{'data':data})		

	@login_required
	@is_admin
	@is_manager
	@is_hr	
	def create(request):
		if request.method == "POST":
			form = DesignationForm(request.POST)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = DesignationModel.objects.all()
				return redirect('/masters/emp_designation',{'data':data})	
			else:
				return render(request,'settings/masters/designation/create.html',{'form':form})
		else:
			form = DesignationForm()
			return render(request,'settings/masters/designation/create.html',{'form':form})				

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def edit(request,id):
		if request.method == "POST":
			obj = DesignationModel.objects.get(id=id)
			form = DesignationForm(request.POST,instance = obj)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = DesignationModel.objects.all()
				return redirect('/masters/emp_designation',{'data':data})	
			else:
				return render(request,'settings/masters/designation/edit.html',{'form':form,'id':id})					
		else:
			obj = DesignationModel.objects.get(id=id)
			form = DesignationForm(instance=obj)
			return render(request,'settings/masters/designation/edit.html',{'form':form,'id':id})

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def delete(request,id):
		depart = DesignationModel.objects.get(id = id)
		depart.delete()
		messages.add_message(request, messages.INFO, 'Data Deleted Successfully.')
		data = DesignationModel.objects.all()
		return redirect('/masters/emp_designation',{'data':data})		

class Grade():

	@login_required
	@is_admin
	@is_manager
	@is_hr
	def index(request):
		data = EmployeeGrade.objects.all()
		return render(request,'settings/masters/grade/index.html',{'data':data})		

	@login_required
	@is_admin
	@is_manager
	@is_hr	
	def create(request):
		if request.method == "POST":
			form = EmployeeGradeForm(request.POST)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = EmployeeGrade.objects.all()
				return redirect('/masters/emp_grade',{'data':data})	
			else:
				return render(request,'settings/masters/grade/create.html',{'form':form})
		else:
			form = EmployeeGradeForm()
			return render(request,'settings/masters/grade/create.html',{'form':form})				

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def edit(request,id):
		if request.method == "POST":
			obj = EmployeeGrade.objects.get(id=id)
			form = EmployeeGradeForm(request.POST,instance = obj)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = EmployeeGrade.objects.all()
				return redirect('/masters/emp_grade',{'data':data})	
			else:
				return render(request,'settings/masters/grade/edit.html',{'form':form,'id':id})					
		else:
			obj = EmployeeGrade.objects.get(id=id)
			form = EmployeeGradeForm(instance=obj)
			return render(request,'settings/masters/grade/edit.html',{'form':form,'id':id})

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def delete(request,id):
		depart = EmployeeGrade.objects.get(id = id)
		depart.delete()
		messages.add_message(request, messages.INFO, 'Data Deleted Successfully.')
		data = EmployeeGrade.objects.all()
		return redirect('/masters/emp_grade',{'data':data})		

class EmpType():

	@login_required
	@is_admin
	@is_manager
	@is_hr
	def index(request):
		data = EmployeeType.objects.all()
		return render(request,'settings/masters/type/index.html',{'data':data})		

	@login_required
	@is_admin
	@is_manager
	@is_hr	
	def create(request):
		if request.method == "POST":
			form = EmployeeTypeForm(request.POST)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = EmployeeType.objects.all()
				return redirect('/masters/emp_type',{'data':data})	
			else:
				return render(request,'settings/masters/type/create.html',{'form':form})
		else:
			form = EmployeeTypeForm()
			return render(request,'settings/masters/type/create.html',{'form':form})				

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def edit(request,id):
		if request.method == "POST":
			obj = EmployeeType.objects.get(id=id)
			form = EmployeeTypeForm(request.POST,instance = obj)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = EmployeeType.objects.all()
				return redirect('/masters/emp_type',{'data':data})	
			else:
				return render(request,'settings/masters/type/edit.html',{'form':form,'id':id})					
		else:
			obj = EmployeeType.objects.get(id=id)
			form = EmployeeTypeForm(instance=obj)
			return render(request,'settings/masters/type/edit.html',{'form':form,'id':id})

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def delete(request,id):
		depart = EmployeeType.objects.get(id = id)
		depart.delete()
		messages.add_message(request, messages.INFO, 'Data Deleted Successfully.')
		data = EmployeeType.objects.all()
		return redirect('/masters/emp_type',{'data':data})		

class EmpStatus():

	@login_required
	@is_admin
	@is_manager
	@is_hr
	def index(request):
		data = EmployeeStatus.objects.all()
		return render(request,'settings/masters/status/index.html',{'data':data})		

	@login_required
	@is_admin
	@is_manager
	@is_hr	
	def create(request):
		if request.method == "POST":
			form = EmployeeStatusForm(request.POST)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = EmployeeStatus.objects.all()
				return redirect('/masters/emp_status',{'data':data})	
			else:
				return render(request,'settings/masters/status/create.html',{'form':form})
		else:
			form = EmployeeStatusForm()
			return render(request,'settings/masters/status/create.html',{'form':form})				

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def edit(request,id):
		if request.method == "POST":
			obj = EmployeeStatus.objects.get(id=id)
			form = EmployeeStatusForm(request.POST,instance = obj)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.INFO, 'Data Successfully Save.')
				data = EmployeeStatus.objects.all()
				return redirect('/masters/emp_status',{'data':data})	
			else:
				return render(request,'settings/masters/status/edit.html',{'form':form,'id':id})					
		else:
			obj = EmployeeStatus.objects.get(id=id)
			form = EmployeeStatusForm(instance=obj)
			return render(request,'settings/masters/status/edit.html',{'form':form,'id':id})

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def delete(request,id):
		depart = EmployeeStatus.objects.get(id = id)
		depart.delete()
		messages.add_message(request, messages.INFO, 'Data Deleted Successfully.')
		data = EmployeeStatus.objects.all()
		return redirect('/masters/emp_status',{'data':data})						
			