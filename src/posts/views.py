from typing import Any
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from posts.models import Post,Postview,Like,Comment
from .forms import PostForm,CommentForm
# Create your views here.

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    success_url = "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context

    
class PostListView(ListView):
    model = Post    
    
class PostDetailView(DetailView):
    model = Post  
    
    def post(self,*args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect('detail_post', slug=post.slug)
        return redirect('detail_post', slug=self.get_object().slug)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm 
        })
        return context
    
    def get_object(self,**kwargs):
        object = super().get_object(**kwargs)
        Postview.objects.get_or_create(user=self.request.user, post=object)
        return object
    
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    success_url = "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context
    
            
class PostDelete(DeleteView):
    model = Post
    success_url = "/"
    

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qr = Like.objects.filter(user=request.user, post=post)
    if like_qr.exists():
        like_qr[0].delete()
        return redirect('detail_post',slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail_post',slug=slug)