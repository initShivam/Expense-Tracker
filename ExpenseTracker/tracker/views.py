from django.shortcuts import render, redirect
from .models import CurrentBalance, HistoryTracker
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required 

def logout_view(request):
    logout(request)
    return redirect('/login/')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if not user.exists():
            messages.success(request, "Username not found") 
            return redirect('/login/')
        
        user = authenticate(request, username = username , password = password)
        if not user:
            messages.success(request, "Incorrect password") 
            return redirect('/login/')        
        auth_login(request , user)
        return redirect('/')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already exists.")
            return redirect('/register/')
        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name =last_name,
        ) 
        user.set_password(password)
        user.save()
        messages.success(request, "Registration successful. You can now log in.")
        return redirect('/login/')
    return render(request,'register.html')


@login_required(login_url='login_view')
def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        try:
            amount = float(request.POST.get('amount'))
        except (TypeError, ValueError):
            messages.error(request, "Invalid amount entered.")
            return redirect('/')

        if amount == 0:
            messages.error(request, "Amount cannot be zero.")
            return redirect('/')

        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)

        expense_type = "DEBIT" if amount < 0 else "CREDIT"

        tracking_history = HistoryTracker.objects.create(
            amount=amount,
            expense_type=expense_type,
            current_balance=current_balance,
            description=description
        )

        current_balance.current_balance += amount
        current_balance.save()
        return redirect('/')

    current_balance, _ = CurrentBalance.objects.get_or_create(id=1)

    income = HistoryTracker.objects.filter(expense_type="CREDIT").aggregate(Sum('amount'))['amount__sum'] or 0
    expense = HistoryTracker.objects.filter(expense_type="DEBIT").aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'income': income,
        'expense': expense,
        'transactions': HistoryTracker.objects.all(),
        'current_balance': current_balance
    }
    return render(request, 'index.html', context)

@login_required(login_url='login_view')
def delete_transaction(request, id):
    tracking_history = HistoryTracker.objects.filter(id=id)
    if tracking_history.exists():
        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
        transaction = tracking_history.first()
        current_balance.current_balance -= float(transaction.amount)
        current_balance.save()
        transaction.delete()
    return redirect('/')