from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from employee.models import User
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        labels = {
             'username':'Username',
             'first_name':'First Name',
             'last_name' :'Last Name',
             'password1':'Password',
             'password2':'Confirm Password',
         }        


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        if commit:
            user.save()
        return user 

class EmployeeEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        labels = {
             'username':'Username',
             'first_name':'First Name',
             'last_name' :'Last Name',
             'email':'Email',
         }        