from django.contrib.auth.forms import UserCreationForm
from hrd.models import Employee
from django.forms import ModelForm


class AddEmployee(ModelForm):
    class Meta(ModelForm):
        model = Employee
        fields = ('__all__')
        # labels = {
        #      'username':'Username',
        #      'first_name':'First Name',
        #      'last_name' :'Last Name',
        #      'password1':'Password',
        #      'password2':'Confirm Password',
        #  }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        if commit:
            user.save()
        return user 
         