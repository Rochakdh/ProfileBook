from django.shortcuts import render
from  django.views.generic import ListView,DeleteView,UpdateView
from  .models import Blog
from .forms import  BlogForm
from django.urls import reverse_lazy
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
    success_url ='/blog/view/'
    form_class = BlogForm
    template_name = 'blog/updateblog.html'

    def get_queryset(self):
        return Blog.objects.filter(author = self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)