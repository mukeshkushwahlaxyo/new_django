from django.forms import ModelForm
from django import forms
from masters.models import DepartmentModel,DocumentTypeModel,DesignationModel,EmployeeGrade,EmployeeStatus,EmployeeType

class DepartmentForm(ModelForm):
	name = forms.CharField(required = True)
	description = forms.CharField(required = False)

	class Meta(ModelForm):
		model = DepartmentModel
		fields = ('name','description')	
		labels = {
				'name':'Name',
				'description':'Description'
			}

class DocumentTypeForm(ModelForm):
	name = forms.CharField(required = True)
	description = forms.CharField(required = False)

	class Meta(ModelForm):
		model = DocumentTypeModel
		fields = ('name','description')	
		labels = {
				'name':'Name',
				'description':'Description'
			}			

class DesignationForm(ModelForm):
	name = forms.CharField(required = True)
	description = forms.CharField(required = False)

	class Meta(ModelForm):
		model = DesignationModel
		fields = ('name','description')
		labels = {
			'name':'Name',
			'description':'Description'
		}

class EmployeeGradeForm(ModelForm):
	name = forms.CharField(required = True)
	description = forms.CharField(required = False)

	class Meta(ModelForm):
		model = EmployeeGrade
		fields = ('name','description')
		labels = {
			'name':'Name',
			'description':'Description'
		}
  

class EmployeeStatusForm(ModelForm):
	name = forms.CharField(required = True)
	description = forms.CharField(required = False)

	class Meta(ModelForm):
		model = EmployeeStatus
		fields = ('name','description')
		labels = {
			'name':'Name',
			'description':'Description'
		}			

class EmployeeTypeForm(ModelForm):
	name = forms.CharField(required = True)
	description = forms.CharField(required = False)

	class Meta(ModelForm):
		model = EmployeeType
		fields = ('name','description')
		labels = {
			'name':'Name',
			'description':'Description'
		}				