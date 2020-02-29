from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from leavemanagement.forms import LeaveTypeForm
from leavemanagement.models import LeaveTypeModel,LeaveApply
from django.core import serializers
from django.contrib.auth.decorators import login_required

from employee.decorators import is_admin,is_employee,is_manager,is_hr

class LeaveType():

	@login_required
	@is_admin
	@is_manager
	@is_hr
	def index(request):
		data = LeaveTypeModel.objects.all();
		return render(request,'leave_manage/leave_type/index.html',{'data':data});

	@login_required
	@is_admin
	@is_manager
	@is_hr	
	def create(request):
		if request.method == 'POST':
			form = LeaveTypeForm(request.POST);
			if form.is_valid():
				form.save()
				data = LeaveTypeModel.objects.all()
				return HttpResponseRedirect('/leave_manage/leavetype');	
			else:
				return render(request,'leave_manage/leave_type/create.html',{'form':form});					
		else:
			form = LeaveTypeForm()
			return render(request,'leave_manage/leave_type/create.html',{'form':form});										

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def showInfo(request):
		data =  LeaveTypeModel.objects.get(id=request.POST['id'])
		data = serializers.serialize('json', [ data, ])
		return JsonResponse({'data':data})		

	@login_required
	@is_admin
	@is_manager
	@is_hr	
	def edit(request,id):
		data = LeaveTypeModel.objects.get(id=id)
		form = LeaveTypeForm(instance=data);
		if request.method == 'POST':
			form = LeaveTypeForm(request.POST,instance=data);
			if form.is_valid():
				form.save()
				data = LeaveTypeModel.objects.all()
				return HttpResponseRedirect('/leave_manage/leavetype');	
			else:
				return render(request,'leave_manage/leave_type/edit.html',{'form':form,'id':id});					
		else:
			return render(request,'leave_manage/leave_type/edit.html',{'form':form,'id':id});	

	@login_required
	@is_admin
	@is_manager
	@is_hr		
	def delete(request,id):
		leave = LeaveTypeModel.objects.get(pk=id)		
		leave.delete()
		return HttpResponseRedirect('/leave_manage/leavetype');	

class LeaveApprove():

	def index(request):
		data = LeaveApply.objects.all()
		return render(request,'leave_manage/LeaveApprove/index.html',{'data':data});	

	def ApproveLeave(request,id,action):
		leaves = LeaveApply.objects.get(id = id)		
		if  request.user.is_manager:
			leaves.teamlead_approval = action
			leaves.save()
		
		if  request.user.is_hr:
			leaves.subadmin_approval = action
			leaves.save()
		
		if  request.user.is_admin:
			leaves.admin_approval = action
			leaves.save()		
		return redirect('/leave_manage/leave_request/')