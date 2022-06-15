from contextvars import Context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Contact
from .forms import AddContactForm

@login_required
def index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        contacts = Contact.objects.filter(username=request.user, firstname__icontains=search)
        return render(request, 'contactapp1/index.html', {'contacts': contacts, 'reset_filter': True})

    contacts = Contact.objects.filter(username=request.user)
    return render(request, 'contactapp1/index.html', {'contacts': contacts})

@login_required
def detail(request, id):
    contacts = Contact.objects.filter(id=id)
    return render(request, 'contactapp1/detail.html', {'contacts': contacts})

@login_required
def add(request):
    if request.method == "POST":
        form = AddContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'contactapp1/add_contact.html')        

@login_required
def delete(request, id):
    get_object_or_404(Contact, id=id).delete()
    return redirect('index')

@login_required
def search(request):
    print(request.GET)
    return render(request, 'contactapp1/search.html')            


@login_required
def edit(request, id):
    contact = get_object_or_404(Contact, id=id)

    form = AddContactForm(request.POST or None, instance=contact)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')
    
    context = {'contact': contact}
    return render(request, 'contactapp1/edit_contact.html', context)

def about(request):
    return render(request, 'contactapp1/about.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, ('Confirm Password is not match'))

            return redirect('register')
        try:
            User.objects.create_user(username=username, email=email, password=password2)
            messages.success(request, ('User registered successfuly'))
        except:
            messages.error(request, ('User can not register successfuly'))
            return redirect('register')

    return render(request, 'contactapp1/register.html')


def login_account(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)

        if auth is not None:
            login(request, auth)
            return redirect('index')

    return render(request, 'contactapp1/login.html')

@login_required
def logout_account(request):
    logout(request)
    return redirect('index')