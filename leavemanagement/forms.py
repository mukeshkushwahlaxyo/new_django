from django.forms import ModelForm
from leavemanagement.models import LeaveTypeModel,LeaveApply
from django import forms

class LeaveTypeForm(ModelForm):
	leave_per_year = forms.CharField(required=False)
	total =forms.CharField(required=False)
	generate_days =forms.CharField(required=False)
	max_apply_once = forms.CharField(required=False)
	min_apply_once = forms.CharField(required=False)
	max_days_month = forms.CharField(required=False)
	max_apply_year = forms.CharField(required=False)
	carry_forward = forms.CharField(required=False)
	docs_required = forms.CharField(required=False)
	without_pay = forms.CharField(required=False)
	dont_show = forms.CharField(required=False)
	max_apply_month = forms.CharField(required=False)

	class Meta(ModelForm):
		model = LeaveTypeModel
		fields = ('name','leave_per_year','total','generate_days','max_apply_once','min_apply_once','max_days_month','max_apply_year','carry_forward','docs_required','without_pay','dont_show','max_apply_month')
		labels = {
			'name' : 'Leave Name',
			'leave_per_year' : 'Leave Per Year',
			'total':'Total leaves',
			'generate_days':'Generate days',
			'max_apply_once':'Can be applied max once',
			'min_apply_once':'Maximum time can be appied in one',
			'max_apply_month':'Maximum time can be appied in month',
			'max_days_month':'Maximum days in a month',
			'max_apply_year':'Can be applied max in year',
			'carry_forward':'Can be carry forward',
			'docs_required':'Document required',
			'without_pay':'Is it LWP?',
			'dont_show':'Dont Show(to employee)',
		}

class LeaveApplyForm(ModelForm):
	
	class Meta(ModelForm):
		model = LeaveApply
		fields = ('leave_type_id','reports_to','date_from','date_to','count','reason','contact_no','applicant_remark','user','admin_approval','subadmin_approval','teamlead_approval')
		labels ={
			'leave_type_id_id':'Leave',	
			'reports_to':'Reports To',
			'date_from':'From(Date)',
			'date_to':'To(Date)',
			'count':'Total Days',
			'reason':'Reason',
			'contact_no':'Contact no',
			'applicant_remark':" 'Applicant's Remark",
		}	