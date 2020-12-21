from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.



class PostListView(ListView):
    model = Post
    context_object_name= 'posts'
    template_name = 'blog/home.html'
    ordering = ['-created']



class PostDetailView(DetailView):
    model = Post
   
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'gender']


    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)