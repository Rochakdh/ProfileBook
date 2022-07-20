from django.shortcuts import render
from  django.views.generic import ListView,DeleteView,UpdateView,DetailView,CreateView
from  .models import Blog
from .forms import  BlogForm
from django.urls import reverse_lazy,reverse
from user.views import UpdateProfile

# Create your views here.

class BlogCreate(CreateView):
    template_name = 'blog/blogcreate.html'
    form_class = BlogForm
    success_url = '/user/profile/'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author =self.request.user
        self.object.save()
        return super(BlogCreate, self).form_valid(form)


class BlogView(ListView):
    template_name = 'blog/yourbloglist.html'

    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user.id)

class BlogDelete(DeleteView):
    model = Blog
    success_url ='/blog/view/'

    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user.id)

class BlogUpdate(UpdateView):
    model = Blog
    template_name = 'blog/updateblog.html'
    form_class = BlogForm
    success_url = '/blog/view/'

    def get_queryset(self):
        return Blog.objects.filter(author= self.request.user)

class AllBlogDetail(DetailView):
    template_name = 'blog/blogdetail.html'
    model = Blog


#blog check to create git branch