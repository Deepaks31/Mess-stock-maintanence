from .models import SavedItem, Item
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def order(request):
    if request.method == 'POST':
        items = request.POST.getlist('item[]')
        quantities = request.POST.getlist('quantity[]')
        needed_date = request.POST.get('needed_date')

        # Ensure input is valid before saving
        for item_name, quantity in zip(items, quantities):
            if item_name.strip() and quantity.strip():
                SavedItem.objects.create(item_name=item_name, quantity=quantity, needed_date=needed_date)

        return redirect('item_list')

    return render(request, 'order.html')

@login_required(login_url='login')
def item_list(request):
    items = Item.objects.all()  
    return render(request, 'item_list.html', {'items': items})

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!")

    return render(request, 'login.html')

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('login')
