from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import UpdateView,RedirectView,ListView,DetailView,CreateView
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import UserTableDetail,SignupForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy,reverse
from blog.models import Blog
from django.http import HttpResponse

USER = get_user_model()
# Create your views here.
class SignupView(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'user/signup.html')

    def post(self,request,*args,**kwargs):
        form = SignupForm(request.POST)
        signupform = {
            'form': form
        }
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = USER.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email = email
            )
            user.set_password(password)
            user.save()
            return redirect('/user/login/')


class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'user/login.html')

    def post(self,request,*args,**kwargs):
        login_param=request.POST.get('login')
        password=request.POST.get('password')
        print(login_param)
        print(password)
        user = authenticate(username=login_param,password=password)
        if user:
            login(request,user)
            return redirect('user:profile')
        else:
            return redirect('user:login')

# class ProfileView(DetailView):
#     template_name = 'user/base.html'

@method_decorator(login_required,name='dispatch')
class ProfileView(ListView):
    template_name = 'user/profile.html'
    model = Blog


class LogoutView(RedirectView):
    url = '/user/login/'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).dispatch(request, *args, **kwargs)




# class UpdateProfile(View):
#     # template_name = 'user/updateprofile.html'
#     # model = get_user_model()
#     # success_url =reverse_lazy('user:update')
#     def get(self, request, *args, **kwargs):
#         print(self.request.user)
#         user_detail = UserTableDetail(instance=self.request.user)
#         context ={
#             'userdetail':user_detail
#         }
#         return render(request, 'user/updateprofile.html',context)

class UpdateProfile(UpdateView):
    template_name = 'user/updateprofile.html'
    model = get_user_model()
    # success_url = reverse_lazy('user:update',kwargs={'pk':1})
    form_class = UserTableDetail

    def get_success_url(self):
        return reverse('user:update',kwargs={'pk':self.object.pk})

class CompleteProfile(View):
    def get(self,request,*args,**kwargs):
        return render(request,'user/updateprofile.html')

class Search(View):
    def get(self,request):
        blogs_list = Blog.objects.filter(title__contains=request.GET.get('title'))
        con_text = {
            'object_list':blogs_list
        }
        return render(request,'user/profile.html',con_text)