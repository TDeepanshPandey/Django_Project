from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from . import forms

# Create your views here.
def index(request):
    return HttpResponse("<em>My second App</em>")

def help(request):
    return render(request, 'appTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_record = {'user':user_list}
    return render(request, 'user/index.html', context=user_record)

def form(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'forms/index.html',{'form':form})