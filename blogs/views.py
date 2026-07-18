from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog,Category

# Create your views here.
def posts_by_category(request,category_id):
    
    #fetch the posts that belongs to the category with the id category id
    posts=Blog.objects.filter(status='Published',category=category_id)
    
    #Use try/except when we want to do some custom action if the category does not exist
    # try:
    #     category=Category.objects.get(pk=category_id)#for one data(use try always)
    # except:
    #     #redirect user to home page
    #     return redirect('home')
    
    #Use get_object_or_404 when you want to show 404 error page if the category does not exit
    category= get_object_or_404(Category,pk=category_id) 

    context={
        'posts':posts,
        'category':category,
    }

    return render(request,'posts_by_category.html',context)