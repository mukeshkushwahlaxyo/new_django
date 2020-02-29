from  django.urls import path
from . import views

urlpatterns = [
	path('leavetype/',views.LeaveType.index,name='leavetype'),
	path('create/',views.LeaveType.create,name='leavetype.create'),
	path('showInfo/',views.LeaveType.showInfo,name='leavetype.showinfo'),
	path('edit/<int:id>',views.LeaveType.edit,name='leavetype.edit'),
	path('delete/<int:id>',views.LeaveType.delete,name='leavetype.delete'),

	# This Route For Approve 
	path('leave_request/',views.LeaveApprove.index,name='leaveapprove.index'),
	path('approve_leave/<int:id>/<slug:action>',views.LeaveApprove.ApproveLeave,name='leaveapprove.ApproveLeave'),

]