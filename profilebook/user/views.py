from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import UserTableDetail
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy



# Create your views here.

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'user/login.html')

    def post(self,request,*args,**kwargs):
        login_param=request.POST.get('login')
        password=request.POST.get('password')
        user = authenticate(username=login_param,password=password)
        if user:
            login(request,user)
            return redirect('user:profile')
        else:
            return redirect('user:login')

# class ProfileView(DetailView):
#     template_name = 'user/base.html'

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/profile.html')

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
    success_url = reverse_lazy('user:update',kwargs={'pk':1})
    form_class = UserTableDetail




