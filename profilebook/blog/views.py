from django.shortcuts import render
from  django.views.generic import ListView,DeleteView,UpdateView,DetailView
from  .models import Blog
from .forms import  BlogForm
from django.urls import reverse_lazy,reverse
from user.views import UpdateProfile

# Create your views here.
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

    def post(self, request, *args, **kwargs):
        self.object= BlogForm.save(self)
        return super().post(request, *args, **kwargs)




class AllBlogDetail(DetailView):
    template_name = 'blog/blogdetail.html'
    model = Blog



