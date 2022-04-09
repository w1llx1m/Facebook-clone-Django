from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import CreateUserForm




class UserCreation(View):

	template_name = 'creation_user.html'

	def get(self, request, *args, **kwars):
		form = CreateUserForm()
		context = {'form': form}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwars):
		form = CreateUserForm(request.POST or None)
		context = {'form': form}
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get("username")
			messages.success(request, 'Account was created for '+user)
			return redirect('login-user')
		return render(request, self.template_name, context)


class UserAuth(View):
	
	template_name = 'login.html'

	def get(self, request, *args, **kwars):
		form = CreateUserForm()
		context = {'form': form}
		return render(request, self.template_name, context)
	
	def post(self,request, *args, **kwars):
		username = request.POST.get('username')
		passwd = request.POST.get('password')
		context = {}
		user = authenticate(request, username=username, password=passwd)
		if user is not None:
			login(request, user)
			return redirect('home')
		return render(request, self.template_name, context)

	
@require_http_methods(["GET"])
def home_view(request, *args, **kwars):
	template_name = 'home.html'
	context = {}
	return render(request, template_name, context)

