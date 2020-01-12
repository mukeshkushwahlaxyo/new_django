from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
# from .forms import SignUpForm
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from rolepermissions.roles import get_user_roles
from django.contrib.auth.decorators import login_required

class Employees:

	@login_required
	def index(request):		
		return render(request, "employees/index.html")