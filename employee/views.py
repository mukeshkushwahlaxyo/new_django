from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from rolepermissions.roles import get_user_roles

class HomePage:

	def index(request):		
		return render(request, "home.html")
	def login(request):
		
		form = AuthenticationForm()
		return render(request, "login.html",{'form':form})

	def checkLogin(request):
		error = {}
		form = AuthenticationForm()
		if request.POST:
		    username = request.POST['username']
		    password = request.POST['password']

		    if form.is_valid():
		    	user = authenticate(username=username, password=password)
		    	if user is not None:
		    		login(request, user)
		    		return redirect("redirect any whre u want")
		    	else:
		    		return render(request, "login.html",{'form':form,'error':'Please enter valid username and password'})
		    else:
		    	return render(request, "login.html",{'form':form,'error':'Please enter username and password'})

		else:
			return render(request, "login.html",{'form':form})

	def Singhup(request):
		form = SignUpForm		
		return render(request, "registration.html",{'form':form})

	def Store(request):	
		form = SignUpForm(request.POST)
		if request.POST:
			if form.is_valid():
				user = form.save()
				# form.refresh_from_db()
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(username=user.username, password=raw_password)
				# user = User.objects.get(id=1)
				assign_role(user, 'is_employee')
				login(request, user)
				if request.user.is_authenticated:
					role = get_user_roles(request.user)
					# return HttpResponse(role)
					# return HttpResponse(request.user.username)
					return redirect('/employee')
			else:
				return render(request, "registration.html",{'form':form})
		else:
			return render(request, "registration.html",{'form':form}) 		
    	


