from django.shortcuts import render
from .models import *
from .forms import CommentForm,SearchForm
from django.core.paginator import Paginator

def Home(request):
    categories = Category.objects.all()
    form = SearchForm(request.POST)
    if not form["name"].value():
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(name=form["name"].value())

    paginator = Paginator(posts,8)
    page_number = request.GET.get('page')
    paginatorPost = paginator.get_page(page_number)

    context = {
        "categories": categories,
        "posts": paginatorPost,
        "form1": form
    }
    return render(request,"project/base.html.twig",{"context":context})

def PostList(request,categoryId):
    form = SearchForm(request.POST)
    if not form["name"].value():
        posts = Post.objects.all().filter(category_id=categoryId)
    else:
        posts = Post.objects.filter(name=form["name"].value())

    categories = Category.objects.all()
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    paginatorPost = paginator.get_page(page_number)

    context = {
        "categories": categories,
        "posts":paginatorPost,
        "form1":form
    }
    return render(request, "project/base.html.twig", {"context":context})

def PostDetail(request,postId):
    categories = Category.objects.all()
    detailPost = Post.objects.filter(id=postId)
    post_view = detailPost.get()
    Post.objects.filter(id=postId).update(view=post_view.view+1)

    form = CommentForm(request.POST)
    form1 = SearchForm(request.POST)

    name = form["name"].value()
    comment = form["comment_text"].value()
    if name and comment:
        comm = Comment(name=name,comment=comment,postId=postId)
        comm.save()
    context = {
        "categories": categories,
        "post":detailPost,
        'form':form,
        "form1":form1
    }

    return render(request,"project/detail.html.twig",{"context":context})

def NewPosts(request):
    categories = Category.objects.all()
    form = SearchForm(request.POST)

    if not form["name"].value():
        posts = Post.objects.all().order_by('-id')
    else:
        posts = Post.objects.filter(name=form["name"].value())

    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    paginatorPost = paginator.get_page(page_number)

    context = {
        "categories": categories,
        "posts": paginatorPost,
        "form1":form
    }
    return render(request,"project/base.html.twig",{"context":context})

def TopPosts(request):
    categories = Category.objects.all()
    form = SearchForm(request.POST)
    if not form["name"].value():
        posts = Post.objects.all().order_by('-view')[:100]
    else:
        posts = Post.objects.filter(name=form["name"].value())
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    paginatorPost = paginator.get_page(page_number)
    context = {
        "categories": categories,
        "posts": paginatorPost,
        "form1":form
    }
    return render(request, "project/base.html.twig",{"context":context})