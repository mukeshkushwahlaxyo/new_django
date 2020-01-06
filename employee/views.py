from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import SignUpForm


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
		form = SignUpForm(request)
		if form.is_valid:
			pass
		else:
			return HttpResponse(form.errors)
    	


