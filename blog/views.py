from django.shortcuts import render
from .models import Category, Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {"posts":posts})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request,'blog/category.html', {"category":category})