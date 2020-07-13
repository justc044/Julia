from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .models import MemberInfo, Category, Blog
import datetime


def signup(request):
    if request.method == 'POST':

        signup_data = request.POST.dict()
        username = signup_data.get("username")
        password = signup_data.get("password")
        name = signup_data.get("name")

        try:
            user = User.objects.create_user(username, email=None, password=password)
        except:
            return HttpResponseRedirect('/accounts/login')

        group = Group.objects.get(name='Guest')
        user.groups.add(group)
        newmemberinfo = MemberInfo(user=user)
        newmemberinfo.name = name
        newmemberinfo.save()

        return HttpResponseRedirect('../accounts/login/')

    return redirect('/accounts/login/')

def loginMember(request):
    if request.method == 'POST':
        signup_data = request.POST.dict()
        username = signup_data.get("username")
        password = signup_data.get("password")

        user = authenticate(username=username, password=password)

        if not request.user.is_anonymous:
            login(request,user)

        if request.user.is_authenticated:
            return redirect('/')
        else:
            return redirect('/accounts/login')
    else:
        return redirect('/accounts/login/')

def signout(request):
    logout(request)

    return redirect('/accounts/login/')

def index(request):

    if request.user.is_authenticated:
        blogs_latest_four = Blog.objects.order_by('-create_date')[:4]

        context = {
            'blogs': blogs_latest_four
        }

        return render(request, 'index.html', context)
    else:
        return redirect('/accounts/login')

def blog_study(request):
    categories_all = Category.objects.all()
    blogs_all = Blog.objects.all()

    context = {
        'categories': categories_all,
        'blogs': blogs_all
    }
    
    return render(request, 'blog_study.html', context)

def blog_add(request):
    categories_all = Category.objects.all()
    member = MemberInfo.objects.get(user = request.user)

    context = {
        'categories': categories_all,
        'member_info': member
    }
    return render(request, 'blog_form.html', context)

def blog_submit(request):
    if request.method == 'POST':
        blog_data = request.POST.dict()

        cat = blog_data.get("category")
        title = blog_data.get("title")
        content = blog_data.get("content")

        category = Category.objects.get(pk=cat)

        new_blog = Blog(user=request.user, category=category, title=title, content=content, create_date=datetime.datetime.now())
        new_blog.save()
        return HttpResponseRedirect('../blog_study')
    return redirect('../blog_study')

def blog_delete(request, pk):
    Blog.objects.filter(pk=pk).delete()
    return redirect('../blog_study')

def portfolio(request):
    return render(request, 'portfolio.html')

def blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    memberinfo = MemberInfo.objects.get(user=blog.user)
    context = {
        'blog': blog,
        'member_info': memberinfo
    }
    return render(request, 'blog.html', context)

def blog_edit(request, pk):
    blog = Blog.objects.get(pk=pk)
    categories_all = Category.objects.all()
    memberinfo = MemberInfo.objects.get(user=blog.user)
    context = {
        'blog': blog,
        'categories': categories_all,
        'member_info': memberinfo
    }
    return render(request, 'blog_form.html', context)

def blog_delete(request, pk):
    Blog.objects.get(pk=pk).delete()
    return HttpResponseRedirect('../blog_study')

def blog_update(request, pk):
    if request.method == 'POST':
        blog_data = request.POST.dict()

        cat = blog_data.get("category")
        title = blog_data.get("title")
        content = blog_data.get("content")

        category = Category.objects.get(pk=cat)

        update_blog = Blog.objects.get(pk=pk)
        update_blog.category = category
        update_blog.title = title
        update_blog.content = content
        update_blog.save()
        return HttpResponseRedirect('../blog_study')
    return redirect('../blog_study')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')