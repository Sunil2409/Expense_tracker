from django.shortcuts import render, redirect
from .models import Expenses
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

def home(request):
    show_expenses = False

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            title = request.POST.get('title')
            amount = request.POST.get('amount')
            category = request.POST.get('category')
            Expenses.objects.create(title=title, amount=amount, category=category)
            return redirect('/')
    
        elif action == 'show':
            show_expenses = True

        
    return render(request, 'tracker/home.html',{
                  'expenses':Expenses.objects.all(), 
                  'show_expenses': show_expenses}
                  )

def login(request):
    if request.method == 'POST':
        action1 = request.POST.get('action1')

        if action1 == 'login':

            username = request.POST.get('username')
            password1 = request.POST.get('password1')

            user = authenticate(request, username = username, password = password1)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login Successful !')
                return redirect('/')
            else:
                messages.error(request, 'Invalid Username or Password')

        elif action1 == 'signup':
            return redirect('sign_up')


    return render(request,'tracker/login.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password2 != password1:
            messages.error(request, "Password doesn't match")
            return redirect('sign_up')
        
        if User.objects.filter(username = username).exists():
            messages.error(request, "User already exists")
            return redirect('sign_up')
        
        User.objects.create_user(username = username,password = password1)
        messages.success(request, "Account Successfully created! ")
        return redirect('login')

    return render(request, 'tracker/sign_up.html')

def sign_out(request):
    logout(request)
    return redirect('login')