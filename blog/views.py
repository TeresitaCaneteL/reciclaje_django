from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic import View
from django.template import Template, Context
from .models import Category, Post

# Create your views here.

class BlogView(View):
  def get(self, request, *args, **kwargs):
    posts = Post.objects.all()
    context={
      'posts':posts

     }
    return render(request, 'blog.html', context)

def category(request, category_id):
  category = get_object_or_404(Category, id=category_id)
  return render(request, 'category.html',{'category':category})