from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from .models import *
from .forms import ContactForm, CreateUserForm
from . guest_utils import *


# Create your views here.
@login_required(login_url='login')
def home_page(request):
    foods = Food.objects.all()
    categories = Category.objects.all()
    if request.method == "POST" and request.POST.get('category_id'):
        category = Category.objects.all()
        foods = Food.objects.filter(category=request.POST.get('category_id'))

    # elif request.method == "GET" and request.POST.get('all_products'):
    #     products = Product.objects.all()

    else:
        foods = Food.objects.all()

    context = {
        'categories': categories,
        'foods': foods,
    }

    return render(request, 'restauranapp/index.html', context)



@login_required(login_url='login')
def allproducts(request):
    foods = Food.objects.all()
    category = Category.objects.all()
    if request.method == "POST" and request.POST.get('category_id'):
        category = Category.objects.all()
        foods = Food.objects.filter(category=request.POST.get('category_id'))

    elif request.method == "GET" and request.POST.get('all_products'):
         foods = Food.objects.all()

    else:
        foods = Food.objects.all()

    context1 = {
        'category': category,
        'foods': foods,
    }

    return render(request, 'restauranapp/allproducts.html', context1)


# Views for adding Card

@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    food = Food.objects.get(id=id)
    cart.add(product=food)
    return redirect("home_page")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    food = Food.objects.get(id=id)
    cart.remove(food)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    food = Food.objects.get(id=id)
    cart.add(product=food)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    food = Food.objects.get(id=id)
    cart.decrement(product=food)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'restauranapp/cart-detail.html')



     





# End card





def registration_user(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        form = CreateUserForm
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('login')

        context = {'form':form}
        return render(request, 'restauranapp/login.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                messages.info(request, "ERORR")
            
        context = {}

        return render(request, 'restauranapp/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def cart_page(request):
    return render(request, 'restauranapp/cart.html')
def about_page(request):
    return render(request, 'restauranapp/about.html')    
""" def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('name')
            return redirect('home')

    context1 = {'form':form}
    return render(request, 'shopapp/contact.html', context1) """


    






def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('name')
            return redirect('home')

    context = {'form':form}
    return render(request, 'restauran/contact.html', context)
