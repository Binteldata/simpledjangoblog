from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category)
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        context = {
            "comments": comments,
            "post": post,
        }
        return render(request, "blog/detail.html", context)