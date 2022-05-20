from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *

menu = [{'title': "About page", 'url_name': 'about'},
        {'title': "Add content", 'url_name': 'add_page'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Log in", 'url_name': 'login'}
]

def index(request):
    posts = Subscription.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Main Page',
        'cat_selected': 0,
    }
    return render(request,'subscription/index.html', context=context)

def about(request):
    return render(request, 'subscription/about.html', {'menu': menu, 'title': 'about page'})

def addpage(request):
    return HttpResponse("add_page")

def contact(request):
    return render(request, 'subscription/contact.html', {'menu': menu, 'title': 'Contact'})

def login(request):
    return render(request, 'subscription/login.html', {'menu': menu,})


def show_post(request, post_id):
    return HttpResponse(f"Post with id = {post_id}")


def show_category(request, cat_id):
    posts = Subscription.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

##    if len(posts) == 0:
##        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Category',
        'cat_selected': cat_id,
    }

    return render(request, 'subscription/index.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')