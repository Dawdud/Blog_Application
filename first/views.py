# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from random import randint
from  first.models import Books, Category, TypeOfDocument
from  first.forms import CategoryForm, BookForm
from django.contrib.auth import login,logout, authenticate
from first.forms import SignUpForm




def index(request):
    Category_List= Category.objects.all()[:5]
    context_dict={'categories': Category_List}
    return render(request, 'first/index.html', context= context_dict)
@permission_required('first.add_books')
def add_Books(request, category_name_slug):
    try:
        category= Category.objects.get(slug= category_name_slug)
    except Category.DoesNotExist:
            category= None
    form= BookForm()
    if request.method=='POST':
        form= BookForm(request.POST)
        if form.is_valid():
            if category:
                book= form.save(commit=False)
                book.category= category
                book.save()
                return show_category(request,category_name_slug)
        else:
            print(form.errors)
    context_dict={'form':form,'category':category}
    return render(request,'first/add_books.html', context_dict)

#@permission_required('first.add_category')
def add_category(request):
    form= CategoryForm()
    if request.method=='POST':
        form= CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index(request)
    else:
        return render(request,'first/add_category.html',{'form':form})


def show_category(request, category_name_slug):
    context_dict= {}
    try:
        category= Category.objects.get(slug= category_name_slug)
        books= Books.objects.filter(category= category)
        context_dict['books']= books
        context_dict['category']= category
    except Category.DoesNotExist:
        context_dict['category']=None
        context_dict['pages']= None
    return render(request,'first/category.html', context_dict)


def show_books(request, book_name_slug, id):
    context_dict={}
    book= get_object_or_404(Books,pk=id)

    try:

        books= Books.objects.get(slugbook=book_name_slug)
        context_dict['books']= books

    except Books.DoesNotExist:
        context_dict['books']= None

    return render(request,'first/Books.html', context_dict)

def signup(request):
    if request.method =='POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form= SignUpForm()
    return render(request,'first/signup.html',{'form':form})


def login_view(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(username= username, password= password)
        if user is not None:
            if user.is_active:
                login(request,user)

                return HttpResponse("Logged in")
            else:
                return HttpResponse("account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'registration/login.html',{})


def logout_view(request):
    logout(request)
    return HttpResponse('Loggin out')

def about(request):
    return HttpResponse("about", )
# Create your views here.
