from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post 
from .forms import PostForm
#from urllib import response
# from django.urls import reverse_lazy, reverse 

# Create your views here.
def index(request):
    # If the method is POST
    if request.method == 'POST':
        
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20]

    return render(request, 'posts.html', {"posts": posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return HttpResponseRedirect('/')

# def edit(request, post_id):
#     post = Post.objects.get(id=post_id)
#     if request.method == 'GET':
#         post=Post.objects.get(id=post_id)
#         return render(request, 'edit.html', {"post":post})
#     if request.method == "POST":
#         editpost = Post.objects.get(id=post_id)
#         form = PostForm(request.POST,request.FILES,instance=editpost)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponseRedirect('not valid')
def edit (request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES, instance =post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, "edit.html",{"post":post})

def LikeView(request, post_id):
    new_value = Post.objects.get(id=post_id)
    new_value.likecount += 1
    new_value.save()
    return HttpResponseRedirect('/')